from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from models import TipoMovimentacao

class MovimentacaoSchema(BaseModel):
    """
    Define como uma nova movimentação a ser inserida deve ser representada
    """
    valor: float = Field(example=150.00)
    tipo: TipoMovimentacao = Field(example='SAIDA')
    data_movimentacao: str = Field(example='18/08/2025 22:30')
    categoria: str = Field(example='Alimentação')
    descricao: Optional[str] = Field(default=None, example='Lanche com a familia')
    contraparte: Optional[str] = Field(default=None, example='BurgerKing')
    usuario_id: int = Field(example=1)


class MovimentacaoDataSchema(BaseModel):
    """Schema para os dados de uma movimentação"""
    id: int = Field(example=1)
    valor: float = Field(example=150.00)
    tipo: str = Field(example='SAIDA')
    data_movimentacao: datetime = Field(example=datetime(2025, 8, 18, 22, 30))
    categoria: str = Field(example='Alimentação')
    descricao: Optional[str] = Field(default=None, example='Lanche com a familia')
    contraparte: Optional[str] = Field(default=None, example='BurgerKing')
    usuario_id: int = Field(example=1)


class MovimentacaoViewSchema(BaseModel):
    """
    Define como uma movimentação será retornada.
    """
    data: MovimentacaoDataSchema
    message: str = Field(example='Exemplo de mensagem')

class ListaMovimetacaoData(BaseModel):
    movimentacoes: List[MovimentacaoDataSchema]
    ultimo_calculo: datetime = Field(example=datetime(2025, 8, 18, 22, 30))
    username: str = Field(example='Teste')
    saldo: float = Field(example=15000)
    usuario_id: int = Field(example=1)

class ListagemMovimentacoesSchema(BaseModel):
    """Define como uma listagem de movimentações será retornada."""
    data: ListaMovimetacaoData   
    message: str = Field(example='Exemplo de mensagem')


class MovimentacaoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca."""
    usuario_id: Optional[int] = Field(None, example=1, description="ID do usuário (opcional)")

class MovimentacaoDeleteSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca."""
    movimentacao_id: Optional[int] = Field(None, example=1, description="ID da movimentação (opcional)")
    usuario_id: Optional[int] = Field(None, example=1, description="ID do usuário (opcional)")

class MovimentacaoUpdateSchema(BaseModel):
    """Schema para os dados de uma movimentação"""
    id: int = Field(example=1)
    valor: float = Field(example=150.00)
    tipo: TipoMovimentacao = Field(example='SAIDA')
    data_movimentacao: str = Field(example='18/08/2025 22:30')
    categoria: str = Field(example='Alimentação')
    descricao: str = Field(default=None, example='Lanche com a familia')
    contraparte: str= Field(default=None, example='BurgerKing')
    usuario_id: int = Field(example=1)