from .movimentacao import (
    MovimentacaoViewSchema, 
    MovimentacaoSchema,
    ListagemMovimentacoesSchema,
    MovimentacaoBuscaSchema, 
    MovimentacaoDataSchema,
    MovimentacaoUpdateSchema,
    MovimentacaoDeleteSchema
    )

from .usuario import UsuarioDataSchema, UsuarioSchema, UsuarioViewSchema

from .resumos import ResumoBuscaSchema, ResumoViewSchema

from .error import ErrorSchema

error_responses = {
    "400": ErrorSchema,
    "404": ErrorSchema,
    "409": ErrorSchema,
    "422": None,
    "500": ErrorSchema,
}


MOV_POST_RESPONSES = {"201": MovimentacaoViewSchema, **error_responses }
MOV_GET_LIST_RESPONSES = {"200": ListagemMovimentacoesSchema, **error_responses}
MOV_PUT_RESPONSES = {"200": MovimentacaoViewSchema, **error_responses}
MOV_DELETE_RESPONSES = {"200": MovimentacaoViewSchema, **error_responses}
USU_REGISTRO_RESPONSE = {"200": UsuarioViewSchema, **error_responses}
USU_AUTH_RESPONSE = {"200": UsuarioViewSchema, **error_responses}
RES_GET_RESPONSES = {"200": ResumoViewSchema, **error_responses}
