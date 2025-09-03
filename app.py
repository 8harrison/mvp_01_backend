from flask_openapi3 import OpenAPI
from flask import redirect
from flask_cors import CORS
from datetime import datetime

from configs.openapi import info, home_tag, movimentacao_tag, usuario_tag, resumo_tag

from models import Usuario

from services import (
    adicionar_movimentacao,
    atualizar_movimentacao,
    listar_movimentacoes,
    excluir_movimentacao,
)

from services import usuario_service
from services.usuario_categoria_mensal_service import get_resumos_de_usuario_por_mes_e_ano

from utils import (
    ADICIONAR_MOVIMENTACAO,
    LISTAR_MOVIMENTACOES,
    ATUALIZAR_MOVIMENTACAO,
    EXCLUIR_MOVIMENTACAO,
    AUTENTICAR_USUARIO,
    REGISTRAR_USUARIO,
    LISTAR_RESUMOS,
    HttpStatus,
    tratar_erros
)

from Dto.movimentacao_dto import MovimentacaoDto
from schemas import (
    MovimentacaoSchema,
    MovimentacaoBuscaSchema,
    UsuarioSchema,
    MovimentacaoUpdateSchema,
    MovimentacaoDeleteSchema,
    ResumoBuscaSchema,
    MOV_POST_RESPONSES,
    MOV_GET_LIST_RESPONSES,
    MOV_PUT_RESPONSES,
    MOV_DELETE_RESPONSES,
    USU_REGISTRO_RESPONSE,
    USU_AUTH_RESPONSE,
    RES_GET_RESPONSES
)

app = OpenAPI(__name__, info=info)
CORS(app)

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post(ADICIONAR_MOVIMENTACAO, tags=[movimentacao_tag], responses=MOV_POST_RESPONSES)
@tratar_erros
def post_movimentacao(body: MovimentacaoSchema):
    """
    Adiciona uma nova movimentação à base de dados.
    """
    nova_movimentacao = MovimentacaoDto(body)
    return adicionar_movimentacao(nova_movimentacao), HttpStatus.CREATED


@app.post(REGISTRAR_USUARIO, tags=[usuario_tag], responses=USU_REGISTRO_RESPONSE)
@tratar_erros
def registrar_usuario(body: UsuarioSchema):
    """
    Registra um novo usuário na base de dados.
    """
    usuario = Usuario(username=body.username,
                      senha=body.senha, saldo=body.saldo)
    return usuario_service.registrar_usuario(usuario)


@app.post(AUTENTICAR_USUARIO, tags=[usuario_tag], responses=USU_AUTH_RESPONSE)
@tratar_erros
def autenticar_usuario(body: UsuarioSchema):
    """
    Autentica um usuário.
    """
    username = body.username
    senha = body.senha
    return usuario_service.logar_usuario(username, senha)


@app.get(LISTAR_MOVIMENTACOES, tags=[movimentacao_tag], responses=MOV_GET_LIST_RESPONSES)
@tratar_erros
def get_movimentacoes(query: MovimentacaoBuscaSchema):
    """
    Faz a busca por todas as movimentações cadastradas.
    """
    usuario_id = query.usuario_id
    return listar_movimentacoes(usuario_id), HttpStatus.OK


@app.put(ATUALIZAR_MOVIMENTACAO, tags=[movimentacao_tag], responses=MOV_PUT_RESPONSES)
@tratar_erros
def update_movimentacao(body: MovimentacaoUpdateSchema):
    """
    Atualiza uma movimentação a partir do id.
    """
    movimentacao_id = body.id
    usuario_id = body.usuario_id
    movimentacao_atualizada = MovimentacaoDto(body)
    return atualizar_movimentacao(movimentacao_id, usuario_id,movimentacao_atualizada), HttpStatus.OK


@app.delete(EXCLUIR_MOVIMENTACAO, tags=[movimentacao_tag], responses=MOV_DELETE_RESPONSES)
@tratar_erros
def delete_movimentacao_por_id(query: MovimentacaoDeleteSchema):
    """
    Deleta uma movimentação a partir do id.
    """
    movimentacao_id = query.movimentacao_id
    usuario_id = query.usuario_id
    return excluir_movimentacao(movimentacao_id, usuario_id), HttpStatus.OK

@app.get(LISTAR_RESUMOS, responses=RES_GET_RESPONSES, tags=[resumo_tag])
@tratar_erros
def get_resumos_por_periodo(query: ResumoBuscaSchema):
    """
    Lista resumos de usuário por ano e mês
    """
    usuario_id = query.usuario_id
    ano = query.ano
    mes = query.mes

    now = datetime.now()
    if not ano:
        ano = now.year
    if not mes:
        mes = now.month

    return get_resumos_de_usuario_por_mes_e_ano(usuario_id, mes, ano)