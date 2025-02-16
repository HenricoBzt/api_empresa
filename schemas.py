from pydantic import BaseModel, EmailStr
from typing import Optional,Literal

class EmpresaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str


class ObrigacaoAcessoriaCreate(BaseModel):
    nome: str
    periodicidade: Literal['mensal','trimestral','anual']
    empresa_id: int

class ObrigacaoAcessoriaBase(BaseModel):
    id: int
    nome: str
    periodicidade: Literal['mensal','trimestral','anual']
    empresa_id: int

