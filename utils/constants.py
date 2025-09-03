# /////////////////////////////////////////////////////
# 
# MENSAGENS DE ERRO
ERRO_FORMATO_DATA = 'Formato de data inválido.'
ERRO_VALOR_MOVIMENTACAO = 'O valor não pode ser negativo ou 0.'
ERRO_TIPO_MOVIMENTACAO = 'O tipo de movimentação deve ser Entrada ou Saida.'
ERRO_MOVIMENTACAO_NOT_FOUND = 'Movimentação não encontrada.'
ERRO_USUARIO_NOT_FOUND = 'Usuário não encontrado.'
ERRO_VALOR_SALDO = 'O saldo não pode ser negativo.'
# 
# //////////////////////////////////////////////////////

# /////////////////////////////////////////////////////
# 
# MENSAGENS DE SUCESSO
class SucessMessages:
    # Mensagens de sucesso para movimentacao
    MOV_CRIADA = 'Movimentação criada.'
    MOV_ENCONTRADA = 'Movimentação encontrada.'
    MOV_EXCLUIDA = 'Movimentação excluída.'
    MOV_ATUALIZADA = 'Movimentação Atualizada.'
    MOV_DISPONIVEIS = 'Movimentações disponíveis.'

    USU_CRIADO = 'Usuário criado.'
    USU_LOGADO = 'Usuário Logado.'
    USU_SALDO_ATUALIZADO = 'Saldo do usuário atualizado.'

    RES_DISPONIVEIS = 'Resumos do período solicitado.'
# 
# //////////////////////////////////////////////////////

# /////////////////////////////////////////////////////
# 
# METODOS HTTP
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
# 
# //////////////////////////////////////////////////////


# /////////////////////////////////////////////////////
# 
####################### ENDPOINTS:

# MOVIMENTACAO:
ADICIONAR_MOVIMENTACAO = '/adicionar_movimentacao'
DETALHAR_MOVIMENTACAO = '/detalhar_movimentacao'
LISTAR_MOVIMENTACOES = '/listar_movimentacoes'
ATUALIZAR_MOVIMENTACAO = '/atualizar_movimentacao'
EXCLUIR_MOVIMENTACAO = '/excluir_movimentacao'

# USUARIO:

REGISTRAR_USUARIO = '/registrar_usuario'
AUTENTICAR_USUARIO = '/autenticar_usuario'

# RESUMO:
LISTAR_RESUMOS = '/listar_resumos'
# 
# //////////////////////////////////////////////////////

# /////////////////////////////////////////////////////
# 
# STATUS DE RESPOSTA HTTP
class HttpStatus:
    # Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    
    # Client errors
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    
    # Server errors
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
# 
# //////////////////////////////////////////////////////




# separador_de_log = '*********////////////////////////*********************'