from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import  Base


class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(20),unique=True,nullable=False)
    endereco = Column(String(200),nullable=False)
    email = Column(String(45),nullable=False)
    telefone = Column(String(14),nullable=False)

    obrigacoes = relationship('ObrigacaoAcessoria',back_populates='empresa',cascade='all, delete')

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"


    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String(200),nullable=False)
    periodicidade = Column(String(45),nullable=False)
    empresa_id = Column(Integer,ForeignKey('empresas.id',ondelete='CASCADE'),nullable=False)

    empresa = relationship("Empresa",back_populates='obrigacoes')

