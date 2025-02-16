import pytest
from schemas import EmpresaBase, ObrigacaoAcessoriaBase
from pydantic import ValidationError


def test_schema_empresabase_valido():
    empresa_valida = EmpresaBase(
        nome= ':Dcifre',
        cnpj= '12.345.678/0001-95',
        endereco= 'Rua Dois',
        email= 'dcifre@gmail.com',
        telefone= '819827640',
    )

    assert empresa_valida.nome == ':Dcifre'
    assert empresa_valida.cnpj == '12.345.678/0001-95'

def test_email_invalido():
    with pytest.raises(ValidationError):
        EmpresaBase(
            nome= ':Dcifre',
            cnpj= '12.345.678/0001-95',
            email= 'dcifremail.com',
            telefone= '819827640'
        )

def test_periodicidade_invalida():
    with pytest.raises(ValidationError):
        ObrigacaoAcessoriaBase(
            nome = 'SPED',
            periodicidade= 'semanal',
            empresa_id= 1
        )

