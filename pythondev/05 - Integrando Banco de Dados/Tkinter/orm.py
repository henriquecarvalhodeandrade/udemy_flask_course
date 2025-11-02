from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

'''criando representação de tabela'''
class Filme(Base):
    __tablename__='filmes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

def add_movie(nome,ano,nota):
    '''inserir dados'''
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome,ano=ano,nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# add_movie('Mario', 2022, 9.8)
# add_movie('Sonic', 2019, 9.5)

def update_movie(id, nome=None,ano=None,nota=None):
    '''atualiza os dados'''
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()

    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

update_movie(1, 'Homem Aranha', 2016, 10)

def delete_movie(id):
    '''exclui filme'''
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    
    if filme:
        session.delete(filme)

    session.commit()
    session.close()

delete_movie(2)