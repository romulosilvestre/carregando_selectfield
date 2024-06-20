from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256


class Usuario(db.Model):
    __tablename__ = "usuario"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(80))
    email  = db.Column(db.String(80))
    senha = db.Column(db.String(255))
    fk_nivel_id= db.Column(db.Integer,db.ForeignKey('nivel.id'))
    nivel = relationship("Nivel",back_populates="usuarios")

    def gen_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def ver_senha(self,senha):
        return pbkdf2_sha256.verify(senha,self.senha)