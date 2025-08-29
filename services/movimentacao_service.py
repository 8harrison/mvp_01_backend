from typing import List

from sqlalchemy.orm import Session as SessionType

from models import Movimentacao
from Dto.movimentacao_dto import MovimentacaoDto
from services import usuario_service
from utils import (
    ERRO_MOVIMENTACAO_NOT_FOUND,
    ERRO_USUARIO_NOT_FOUND,
    response_formatter,
    SucessMessages,
    NotFoundError,
    with_session
)


@with_session
def adicionar_movimentacao(movimentacaoDto: MovimentacaoDto, session):
    usuario_id = movimentacaoDto.usuario_id

    novaMovimentacao = movimentacaoDto.get_movimentacao()
    usuario_service.atualizar_saldo(usuario_id, novaMovimentacao)

    return response_formatter(
        novaMovimentacao.movimentacao_to_json(),
        SucessMessages.MOV_CRIADA
    )

@with_session
def excluir_movimentacao(id, usuario_id, session: SessionType):
    query_movimentacao = session.query(
        Movimentacao).filter(Movimentacao.id == id)

    movimentacao: Movimentacao = query_movimentacao.first()

    if not movimentacao:
        raise NotFoundError(ERRO_MOVIMENTACAO_NOT_FOUND)

    usuario_service.excluir_movimentacao(usuario_id, movimentacao)
    count = query_movimentacao.delete()

    session.commit()

    if count == 1:
        return response_formatter(
            movimentacao.movimentacao_to_json(),
            SucessMessages.MOV_EXCLUIDA
        )
    else:
        raise NotFoundError(ERRO_MOVIMENTACAO_NOT_FOUND)


def get_movimentacao(movimentacao_id, session: SessionType) -> Movimentacao:
    movimentacao = session.query(Movimentacao).filter(
        Movimentacao.id == movimentacao_id).first()
    if not movimentacao:
        raise NotFoundError(ERRO_MOVIMENTACAO_NOT_FOUND)
    return movimentacao


def update_movimentacao(id, movimentacao: Movimentacao, session: SessionType):
    movimentacao_dict = movimentacao.movimentacao_to_json()
    movimentacao_dict.pop('id', None)
    movimentacao_dict.pop('usuario_id', None)
    movimentacao_dict['usuario'] = movimentacao.usuario
    count = session.query(Movimentacao).filter(
        Movimentacao.id == id).update(movimentacao_dict)

    session.commit()
    return count

@with_session
def atualizar_movimentacao(id, usuario_id, movimentacao_dto: MovimentacaoDto, session: SessionType):
    movimentacao_dto.usuario_id = usuario_id
    atualizando_movimentacao = movimentacao_dto.get_movimentacao()
    movimentacao: Movimentacao = get_movimentacao(id, session)
    valor_antigo = movimentacao.valor

    count = update_movimentacao(id, atualizando_movimentacao, session)

    usuario_service.atualizando_movimentacao(
        usuario_id, valor_antigo, atualizando_movimentacao)

    if count == 1:
        # Recarregar o objeto atualizado do banco
        movimentacao_atualizada = get_movimentacao(id, session)
        return response_formatter(
            movimentacao_atualizada.movimentacao_to_json(),
            SucessMessages.MOV_ATUALIZADA
        )
    else:
        raise NotFoundError(ERRO_MOVIMENTACAO_NOT_FOUND)

@with_session
def listar_movimentacoes(usuario_id: int, session: SessionType):
    usuario = usuario_service.get_usuario(usuario_id, session)
    if not usuario:
        raise NotFoundError(ERRO_USUARIO_NOT_FOUND)
    movimentacoes = session.query(Movimentacao).filter(
        Movimentacao.usuario == usuario_id).all()
    return response_formatter(
        apresenta_movimentacoes(movimentacoes),
        SucessMessages.MOV_DISPONIVEIS
    )


def apresenta_movimentacoes(movimentacoes: List[Movimentacao]):
    result = []
    for movimentacao in movimentacoes:
        result.append(movimentacao.movimentacao_to_json())

    return result
