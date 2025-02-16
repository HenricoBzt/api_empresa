from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from settings import Settings


engine = create_engine(Settings().DATABASE_URL)
Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


