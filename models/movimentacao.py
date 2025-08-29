from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, Enum

from models import Base
from enum import Enum as PyEnum

class TipoMovimentacao(PyEnum):
    ENTRADA = 'ENTRADA'
    SAIDA = 'SAIDA'

class Movimentacao(Base):
    __tablename__ = 'movimentacao'

    # id é o Primary key da tabela
    id = Column(Integer, primary_key=True)
    # tipo da movimentação: Entrada ou saída de dinheiro
    tipo = Column(Enum(TipoMovimentacao))
    # valor da movimentação realizada
    valor = Column(Float(2))
    # Data em que fora realizada a movimentação
    data_movimentacao = Column(DateTime)
    # Categorias das entradas ou saidas
    # Exemplos de saída: Alimentação, transporte, Investimento.
    # Exemplos de entrada: Salário, bonus, vendas, PLR, etc.
    categoria = Column(String(40))
    # Comentários adicionais referentes à movimentação.
    descricao = Column(String(4000))
    # Parte oposta na transação financeira, tanto para entradas
    # quanto para saídas. Pode ser utilizados tanto para pessoas
    # quanto para empresas.
    contraparte = Column(String(80))
    # Definição do relacionamento entre a movimentação e um usuario.
    # Aqui está sendo definido a coluna 'usuario' que vai guardar
    # a referencia ao usuario, a chave estrangeira que relaciona
    # um usuario à movimentação.
    usuario = Column(Integer, ForeignKey("usuario.usuario_id"), nullable=False)

    def __init__(
            self,
            tipo: TipoMovimentacao,
            valor: float,
            data_movimentacao: DateTime,
            categoria: str,
            descricao: str,
            contraparte: str,
            usuario_id
            ):
        """
        Cria uma Movimentacao

        Arguments:
            tipo: Entrada ou Saída.
            valor: valor realizado na movimentacao.
            data_movimentacao: data em que a movimentacao foi realizada.
        """

        self.tipo = tipo
        self.valor = valor
        self.data_movimentacao = data_movimentacao
        self.categoria = categoria
        self.descricao = descricao
        self.contraparte = contraparte
        self.usuario = usuario_id

    # Converte o objeto movimentacao para JSON
    def movimentacao_to_json(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "tipo": self.tipo.name,
            "data_movimentacao": self.data_movimentacao,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "contraparte": self.contraparte,
            "usuario_id": self.usuario
        }

