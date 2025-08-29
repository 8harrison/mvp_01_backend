from flask_openapi3 import Info, Tag

HOME_NAME = 'Documentação'
HOME_DSCRPTN = 'Seleção de documentação: Swagger, Redoc ou RapiDoc'

# Parametros de tag para movimentacao
MOV_NAME = 'Movimentação'
MOV_DSCRPTN = 'Adição, visualização, atualização e remoção de movimentações à base'

USU_NAME = 'Usuário'
USU_DSCRPTN = 'Registra e Autentica usuário à base'

info = Info(title="API de Gestão Financeira", version="1.0.0")

# Definindo tags
home_tag = Tag(name=HOME_NAME, description=HOME_DSCRPTN)
movimentacao_tag = Tag(name=MOV_NAME, description=MOV_DSCRPTN)
usuario_tag = Tag(name=USU_NAME, description=USU_DSCRPTN)