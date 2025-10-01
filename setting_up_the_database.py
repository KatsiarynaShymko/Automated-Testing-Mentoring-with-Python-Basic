from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///films_db', echo=False)

Base = declarative_base()

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

def create_tables():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

