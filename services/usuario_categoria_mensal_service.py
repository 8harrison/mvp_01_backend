from sqlalchemy import event, inspect
from sqlalchemy.orm import Session
from typing import List

from models import Movimentacao, UsuarioCategoriaMensal
from utils import with_session, response_formatter, SucessMessages


@event.listens_for(Movimentacao, "after_update")
def after_update_movimentacao(mapper, connection, target: Movimentacao):
    """Atualiza resumo após alterar movimentação"""
    session = Session(bind=connection)
    resumo, ano, mes, tipo = _get_resumo(session, target)

    if resumo:
        hist = inspect(target).attrs.valor.history
        if hist.deleted and hist.added:
            valor_antigo = hist.deleted[0]
            valor_novo = hist.added[0]

            resumo.valor_total -= int(valor_antigo)
            resumo.valor_total += int(valor_novo)

    session.flush()
    session.close()


def _get_resumo(session: Session, target: Movimentacao):
    """Busca ou cria um resumo mensal para a movimentação"""
    ano = target.data_movimentacao.year
    mes = target.data_movimentacao.month
    tipo = target.tipo.name if hasattr(target.tipo, "name") else target.tipo

    return session.query(UsuarioCategoriaMensal).filter_by(
        usuario_id=target.usuario,
        ano=ano,
        mes=mes,
        categoria=target.categoria,
        tipo=tipo
    ).first(), ano, mes, tipo


@event.listens_for(Movimentacao, "after_insert")
def after_insert_movimentacao(mapper, connection, target: Movimentacao):
    """Atualiza resumo após criar movimentação"""
    session = Session(bind=connection)

    resumo, ano, mes, tipo = _get_resumo(session, target)

    if resumo:
        resumo.valor_total += int(target.valor)
    else:
        resumo = UsuarioCategoriaMensal(
            usuario_id=target.usuario,
            ano=ano,
            mes=mes,
            categoria=target.categoria,
            tipo=tipo,
            valor_total=target.valor
        )
        session.add(resumo)

    session.commit()


@event.listens_for(Movimentacao, "after_delete")
def after_delete_movimentacao(mapper, connection, target: Movimentacao):
    """Atualiza resumo após deletar movimentação"""

    session = Session(bind=connection)

    resumo, ano, mes, tipo = _get_resumo(session, target)

    if resumo:
        resumo.valor_total -= int(target.valor)
        if resumo.valor_total <= 0:
            session.delete(resumo)

    session.commit()

@with_session
def get_resumos_de_usuario_por_mes_e_ano(usuario_id: int, mes: int, ano: int, session: Session):
    resumos = session.query(UsuarioCategoriaMensal).filter( 
        UsuarioCategoriaMensal.usuario_id == usuario_id,
        UsuarioCategoriaMensal.mes == mes,
        UsuarioCategoriaMensal.ano == ano
        ).all()
    
    return response_formatter(
        converte_lista_to_json(resumos),
        SucessMessages.RES_DISPONIVEIS
    )
    

def converte_lista_to_json(resumos: List[UsuarioCategoriaMensal]):
    return list(map(lambda r: r.to_json(), resumos))