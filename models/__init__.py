from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Importando os elementos definidos no modelo
from models.base import Base
from models.movimentacao import Movimentacao, TipoMovimentacao
from models.usuario import Usuario
from models.usuario_categoria_mensal import UsuarioCategoriaMensal

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///database/db.sqlite3'

# Cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Insatancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# Cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)


# Cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)