from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

from models import Base



class UsuarioCategoriaMensal(Base):
    __tablename__ = "usuario_categoria_mensal"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey(
        "usuario.usuario_id"), nullable=False)
    ano = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    categoria = Column(String(100), nullable=False)
    tipo = Column(String(10), nullable=False)
    valor_total = Column(Numeric(12, 2), nullable=False, default=0)

    def to_json(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "ano": self.ano,
            "mes": self.mes,
            "categoria": self.categoria,
            "tipo": self.tipo,
            "valor_total": self.valor_total
        }