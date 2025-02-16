import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database import Base
from models import Empresa


db_local = "sqlite:///:memory:" 
engine = create_engine(db_local,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

@pytest.fixture(scope='function')
def session():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


def test_criar_empresa(session: Session):
    empresa = Empresa(
        nome=":Dcifre",
        cnpj="14.525.467/0001-33",
        endereco="Rua Dois, 123",
        email="dcifre@email.com",
        telefone="819739002"
    )

    session.add(empresa)
    session.commit()
    session.refresh(empresa)

    assert empresa.id is not None 
    assert empresa.nome == ":Dcifre"
    assert empresa.cnpj == "14.525.467/0001-33"


def test_buscar_empresa_por_id(session: Session):
    empresa = Empresa(
        nome=":Dcifre",
        cnpj="14.525.467/0001-33",
        endereco="Rua Dois, 123",
        email="dcifre@email.com",
        telefone="819739002"
    )

    session.add(empresa)
    session.commit()
    session.refresh(empresa)

    empresa_db = session.get(Empresa, empresa.id)
    
    assert empresa_db is not None
    assert empresa_db.email == "dcifre@email.com"

def test_atualizar_empresa(session: Session):
    empresa = Empresa(
        nome=":Pjotão",
        cnpj="11.222.333/0001-55",
        endereco="Rua Antiga",
        email="pjotao@email.com",
        telefone="11999999999"
    )

    session.add(empresa)
    session.commit()
    session.refresh(empresa)


    empresa.nome = ":Pjotinha"
    empresa.email = "pjotinha@email.com"
    session.commit()
    session.refresh(empresa)

    assert empresa.nome == ":Pjotinha"
    assert empresa.email == "pjotinha@email.com"

def test_criar_empresa_cnpj_duplicado(session: Session):
    empresa_a = Empresa(
        nome=":Dcifre",
        cnpj="14.525.467/0001-33",
        endereco="Rua Dois, 123",
        email="dcifre@email.com",
        telefone="819739002"
    )

    empresa_b = Empresa(
        nome=":Pjotão",
        cnpj="14.525.467/0001-33",
        endereco="Rua Antiga",
        email="pjotao@email.com",
        telefone="11999999999"
    )

    session.add(empresa_a)
    session.commit()

    with pytest.raises(Exception): 
        session.add(empresa_b)
        session.commit()







