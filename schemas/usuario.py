from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UsuarioSchema(BaseModel):
    """
    Define como um novo usuário a ser inserido deve ser representado
    """
    username: str = Field(example='Teste')
    senha: str = Field(example='123456')
    saldo: Optional[float] = Field(example=10.00)


class UsuarioDataSchema(BaseModel):
    """Schema para os dados de um usuário"""
    usuario_id: int = Field(example=1)
    username: str = Field(example='Teste')
    senha: str = Field(example='123456')
    saldo: float = Field(example=10.00)
    ultimo_calculo: datetime = Field(example=datetime.now())
    created_at: datetime = Field(example=datetime.now())

class UsuarioViewSchema(BaseModel):
    """
    Define como um usuário será retornado.
    """
    data: UsuarioDataSchema
    message: str = Field(example='Exemplo de mensagem')