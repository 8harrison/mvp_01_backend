from sqlalchemy import Column, String, Integer, Float, DateTime
from typing import List

from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base, Movimentacao
from configs.cripto_config import GerenciadorSenhas, KEY_PROVISORIA


class Usuario(Base):
    __tablename__ = 'usuario'

    usuario_id = Column(Integer, primary_key=True)

    username = Column(String(100), unique=True)

    senha = Column(String(100))

    saldo = Column(Float(2), default=0.00)

    ultimo_calculo = Column(DateTime)

    created_at = Column(DateTime, default=datetime.now())

    movimentacoes = relationship('Movimentacao')

    def __init__(self, username: str, senha: str, saldo: float):
        self.username = username
        self.criptografar_senha(senha)
        self.saldo = saldo
        self.ultimo_calculo = datetime.now()

    def criptografar_senha(self, senha: str):
        created_at = datetime.now()
        gerenciador = GerenciadorSenhas(pepper=str(created_at) + KEY_PROVISORIA)
        self.senha = gerenciador.criptografar_senha(senha)
        self.created_at = created_at

    def _validar_senha(self, senha: str):
        gerenciador = GerenciadorSenhas(pepper=str(self.created_at) + KEY_PROVISORIA)
        return gerenciador.validar_senha(senha, self.senha)

    # Converte o objeto usuario para JSON
    def usuario_to_json(self):
        return {
            "usuario_id": self.usuario_id,
            "username": self.username,
            "saldo": self.saldo,
            "ultimo_calculo": self.ultimo_calculo,
            "movimentacoes": self.apresenta_movimentacoes(self.movimentacoes)
        }
    
    def adicionar_movimentacao(self, movimentacao: Movimentacao):
        """ Adiciona uma nova movimentação ao Usuário.
        """
        self.movimentacoes.append(movimentacao)

    def apresenta_movimentacoes(self, movimentacoes: List[Movimentacao]):
        result = []
        for movimentacao in movimentacoes:
            result.append(movimentacao.movimentacao_to_json())

        return result