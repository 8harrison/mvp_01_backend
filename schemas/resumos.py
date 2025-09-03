from pydantic import BaseModel, Field
from typing import List, Optional

class ResumoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca."""
    usuario_id: int = Field(example=1, description="ID do usuário")
    ano: Optional[int] = Field(example=2025)
    mes: Optional[int] = Field(example=8)

class ResumoDataSchema(BaseModel):
    """Schema para os dados de resumo."""
    ano: int = Field(example=2025)
    categoria: str = Field(example='Alimentação')
    id: int = Field(example=1)
    mes: int = Field(example=8)
    tipo: str = Field(example="SAIDA")
    usuario_id: int = Field(example=1)
    valor_total: int = Field(example=1550.00)

class ResumoViewSchema(BaseModel):
    """
    Define como resumos será retornado.
    """
    data: List[ResumoDataSchema]
    message: str = Field(example='Exemplo de mensagem')