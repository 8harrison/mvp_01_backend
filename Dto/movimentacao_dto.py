from models import Movimentacao
from datetime import datetime

from utils.constants import (
    ERRO_FORMATO_DATA,
    ERRO_VALOR_MOVIMENTACAO,
    ERRO_TIPO_MOVIMENTACAO
)

from schemas import MovimentacaoSchema


class MovimentacaoDto:

    def __init__(self, schema: MovimentacaoSchema):
        self.extrai_objeto(schema)
        self.verificar_valor()
        self.verificar_tipo()
        self.movimentacao = Movimentacao(
            tipo=self.tipo,
            valor=self.valor,
            data_movimentacao=self.data_movimentacao,
            categoria=self.categoria,
            descricao=self.descricao,
            contraparte=self.contraparte,
            usuario_id=self.usuario_id
            )

    def get_movimentacao(self) -> Movimentacao:
        return self.movimentacao

    def verificar_valor(self):
        if self.valor <= 0:
            raise ValueError(ERRO_VALOR_MOVIMENTACAO)

    def verificar_tipo(self):
        tipo = self.tipo
        if tipo.name != 'ENTRADA' and tipo.name != 'SAIDA':
            raise ValueError(ERRO_TIPO_MOVIMENTACAO)

    def verificar_data(self, data):
        """
        Recebe uma string e tenta converter para datetime.
        Retorna o objeto datetime se válido, ou None se inválido.
        """
        formatos = [
            "%Y-%m-%d %H:%M:%S",   # exemplo: 2025-08-19 15:30:00
            "%Y-%m-%d %H:%M",      # exemplo: 2025-08-19 15:30
            # exemplo: 2025-08-19T15:30 (input datetime-local HTML5)
            "%Y-%m-%dT%H:%M",
            "%d/%m/%Y %H:%M:%S",   # exemplo: 19/08/2025 15:30:00
            "%d/%m/%Y %H:%M"       # exemplo: 19/08/2025 15:30
        ]

        for fmt in formatos:
            try:
                return datetime.strptime(data, fmt)
            except ValueError:
                continue
        raise ValueError(ERRO_FORMATO_DATA)

    # Função para extrair o objeto MovimentacaoDto do corpo da requisição
    def extrai_objeto(self, schema: MovimentacaoSchema):
        self.valor = schema.valor
        self.tipo = schema.tipo
        self.data_movimentacao = self.verificar_data(schema.data_movimentacao)
        self.categoria = schema.categoria
        self.descricao = schema.descricao
        self.contraparte = schema.contraparte
        self.usuario_id = schema.usuario_id
        