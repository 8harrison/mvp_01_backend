from sqlalchemy.orm import Session as SessionType
from datetime import datetime

from models import Usuario, Movimentacao, TipoMovimentacao
from utils import (
    response_formatter,
    SucessMessages,
    ERRO_USUARIO_NOT_FOUND,
    ERRO_VALOR_SALDO,
    NotFoundError,
    with_session
)


@with_session
def registrar_usuario(usuario: Usuario, session: SessionType):

    session.add(usuario)
    session.commit()
    return response_formatter(usuario.usuario_to_json(),
                              SucessMessages.USU_CRIADO)


@with_session
def logar_usuario(username: str, senha: str, session: SessionType):

    usuario: Usuario = session.query(Usuario).filter(
        Usuario.username == username).first()

    if not usuario:
        raise NotFoundError(ERRO_USUARIO_NOT_FOUND)

    senha_validada = usuario._validar_senha(senha)

    if senha_validada:
        return response_formatter(
            usuario.usuario_to_json(),
            SucessMessages.USU_LOGADO
        )


def get_usuario(usuario_id: int, session: SessionType) -> Usuario:
    usuario = session.query(Usuario).filter(
        Usuario.usuario_id == usuario_id).first()
    if not usuario:
        raise NotFoundError(ERRO_USUARIO_NOT_FOUND)
    return usuario


@with_session
def atualizar_saldo(usuario_id: int, movimentacao: Movimentacao, session: SessionType):

    usuario = get_usuario(usuario_id, session)

    usuario.saldo = calcula_saldo(
        usuario.saldo, movimentacao.tipo, movimentacao.valor)
    usuario.adicionar_movimentacao(movimentacao)
    usuario.ultimo_calculo = datetime.now()

    session.commit()

    return response_formatter(usuario.usuario_to_json(), SucessMessages.USU_SALDO_ATUALIZADO)


@with_session
def atualizando_movimentacao(usuario_id: int, valor_antigo: float, movimentacao: Movimentacao, session: SessionType):

    usuario = get_usuario(usuario_id, session)

    # Retira valor antigo antes de recalcular
    saldo_temp = usuario.saldo - valor_antigo
    usuario.saldo = calcula_saldo(
        saldo_temp, movimentacao.tipo, movimentacao.valor)

    usuario.ultimo_calculo = datetime.now()
    session.commit()
    return response_formatter(usuario.usuario_to_json(), SucessMessages.USU_SALDO_ATUALIZADO)


@with_session
def excluir_movimentacao(usuario_id: int, movimentacao: Movimentacao, session: SessionType):

    usuario = get_usuario(usuario_id, session)

    # Ajusta o valor
    atuali_valor = movimentacao.valor * -1
    usuario.saldo = calcula_saldo(
        usuario.saldo, movimentacao.tipo, atuali_valor)

    usuario.ultimo_calculo = datetime.now()
    session.commit()
    return response_formatter(usuario.usuario_to_json(), SucessMessages.USU_SALDO_ATUALIZADO)


def calcula_saldo(saldo: float, tipoMovimentacao: TipoMovimentacao, valor: float):
    if tipoMovimentacao.name == 'SAIDA':
        saldo -= valor
        if saldo < 0:
            raise ValueError(ERRO_VALOR_SALDO)
    if tipoMovimentacao.name == 'ENTRADA':
        saldo += valor
    return round(saldo, 2)
