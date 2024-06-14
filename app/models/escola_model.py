from app import db
from sqlalchemy.orm import relationship

class Escola(db.Model):
    __tablename__ = "escola"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    telefone= db.Column(db.String(25), nullable=False)
    cursos = relationship("Curso", back_populates="escola")

