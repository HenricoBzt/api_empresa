from fastapi import FastAPI, Depends, HTTPException
from models import Empresa, ObrigacaoAcessoria
from http import HTTPStatus
from database import get_db
from schemas import EmpresaBase, ObrigacaoAcessoriaBase, ObrigacaoAcessoriaCreate
from sqlalchemy.orm import Session
from sqlalchemy import select, or_

app = FastAPI(
    title="Gestor de Empresas API",
    description="API para gerenciamento de empresas e obrigações acessórias.",
    version="1.0.0"
)


@app.post('/empresas/', status_code=HTTPStatus.CREATED, response_model=EmpresaBase,tags=["Empresas"] ,summary='Criar Nova Empresa',description='O endpoint atual cria uma nova empresa')
def create_empresa(empresa: EmpresaBase, session: Session = Depends(get_db)):
    empresa_db = session.scalar(
        select(Empresa).where(or_(Empresa.cnpj == empresa.cnpj, Empresa.email == empresa.email))
    )
    
    if empresa_db:
        if empresa_db.cnpj == empresa.cnpj:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='CNPJ já cadastrado.')
        elif empresa_db.email == empresa.email:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='E-mail já cadastrado')
    
    nova_empresa_db = Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        endereco=empresa.endereco,
        email=empresa.email,
        telefone=empresa.telefone
    )
    session.add(nova_empresa_db)
    session.commit()
    session.refresh(nova_empresa_db)
    return nova_empresa_db

@app.get('/empresas/', status_code=HTTPStatus.OK, response_model=list[EmpresaBase],tags=["Empresas"], summary='Lista Empresa',description='O endpoint atual lista uma empresa')
def list_empresa(session: Session = Depends(get_db)):
    empresas = session.scalars(select(Empresa)).all()
    return empresas

@app.get('/empresas/{empresa_id}', status_code=HTTPStatus.OK, response_model=EmpresaBase, tags=["Empresas"], summary='Lista Empresa Específica',description='O endpoint atual lista uma empresa especificada pelo id')
def get_empresa(empresa_id: int, session: Session = Depends(get_db)):
    empresa_db = session.scalar(select(Empresa).where(Empresa.id == empresa_id))
    
    if not empresa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Empresa não encontrada')
    return empresa_db

@app.put('/empresas/{empresa_id}', response_model=EmpresaBase,tags=["Empresas"],summary='Atualiza uma Empresa',description='O endpoint atual atualiza empresa')
def update_empresa(empresa_id: int, empresa: EmpresaBase, session: Session = Depends(get_db)):
    empresa_db = session.scalar(select(Empresa).where(Empresa.id == empresa_id))
    
    if not empresa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Empresa não encontrada na base de dados')
    
    empresa_db.nome = empresa.nome
    empresa_db.cnpj = empresa.cnpj
    empresa_db.endereco = empresa.endereco
    empresa_db.email = empresa.email
    empresa_db.telefone = empresa.telefone
    
    session.commit()
    session.refresh(empresa_db)
    return empresa_db

@app.delete('/empresas/{empresa_id}', status_code=HTTPStatus.NO_CONTENT,tags=["Empresas"] ,summary='Deleta uma Empresa',description='O endpoint atual deleta uma empresa')
def delete_empresa(empresa_id: int, session: Session = Depends(get_db)):
    empresa_db = session.scalar(select(Empresa).where(Empresa.id == empresa_id))
    
    if not empresa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Empresa não encontrada na base de dados')
    
    session.delete(empresa_db)
    session.commit()
    return None

@app.post('/obrigacoes/', status_code=HTTPStatus.CREATED, response_model=ObrigacaoAcessoriaCreate,tags=["Obrigações Acessórias"], summary="Criar uma nova obrigação acessória",description="Este endpoint permite a criação de uma nova obrigação acessória associada a uma empresa existente.")
def create_acessoria(obrigacao_acessoria: ObrigacaoAcessoriaBase, session: Session = Depends(get_db)):
    empresa_db = session.scalar(select(Empresa).where(Empresa.id == obrigacao_acessoria.empresa_id))
   
    if not empresa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Empresa não encontrada')
    
    acessoria_db = ObrigacaoAcessoria(
        nome=obrigacao_acessoria.nome,
        periodicidade=obrigacao_acessoria.periodicidade,
        empresa_id=obrigacao_acessoria.empresa_id
    )
    session.add(acessoria_db)
    session.commit()
    session.refresh(acessoria_db)
    return acessoria_db

@app.get('/obrigacoes/', status_code=HTTPStatus.OK, response_model=list[ObrigacaoAcessoriaCreate],tags=["Obrigações Acessórias"], summary="Listar todas as obrigações acessórias",description="Retorna uma lista com todas as obrigações acessórias cadastradas no sistema.")
def list_acessorias(session: Session = Depends(get_db)):
    acessorias = session.scalars(select(ObrigacaoAcessoria)).all() 
    return acessorias 

@app.get('/obrigacoes/{obrigacao_acessoria_id}', status_code=HTTPStatus.OK, response_model=ObrigacaoAcessoriaCreate,tags=["Obrigações Acessórias"], summary="Buscar uma obrigação acessória por ID",description="Busca e retorna uma obrigação acessória específica com base no ID informado.")
def get_acessoria(obrigacao_acessoria_id: int, session: Session = Depends(get_db)):
    acessoria_db = session.scalar(select(ObrigacaoAcessoria).where(ObrigacaoAcessoria.id == obrigacao_acessoria_id))
    
    if not acessoria_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Obrigação acessória não encontrada')
    return acessoria_db

@app.put('/obrigacoes/{obrigacao_acessoria_id}', response_model=ObrigacaoAcessoriaCreate, tags=["Obrigações Acessórias"], summary="Atualizar uma obrigação acessória",description="Atualiza os dados de uma obrigação acessória existente com base no ID informado.")
def update_acessoria(obrigacao_acessoria_id: int, obrigacao_acessoria: ObrigacaoAcessoriaBase, session: Session = Depends(get_db)):
    acessoria_db = session.scalar(select(ObrigacaoAcessoria).where(ObrigacaoAcessoria.id == obrigacao_acessoria_id))
    
    if not acessoria_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Obrigação acessória não encontrada na base de dados')
    
    acessoria_db.nome = obrigacao_acessoria.nome
    acessoria_db.periodicidade = obrigacao_acessoria.periodicidade
    acessoria_db.empresa_id = obrigacao_acessoria.empresa_id
    
    session.commit()
    session.refresh(acessoria_db)
    return acessoria_db

@app.delete('/obrigacoes/{obrigacao_acessoria_id}', status_code=HTTPStatus.NO_CONTENT,tags=["Obrigações Acessórias"], summary="Deletar uma obrigação acessória",description="Deleta uma obrigação acessória existente com base no ID informado.")
def delete_acessoria(obrigacao_acessoria_id: int, session: Session = Depends(get_db)):
    acessoria_db = session.scalar(select(ObrigacaoAcessoria).where(ObrigacaoAcessoria.id == obrigacao_acessoria_id))
    
    if not acessoria_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Obrigação acessória não encontrada na base de dados')
    
    session.delete(acessoria_db)
    session.commit()
    return None
