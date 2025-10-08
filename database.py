"""Database configuration: connection setup and metadata creation"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///films_db.sqlite3", echo=False, future=True)
Session = sessionmaker(bind=engine, future=True)


class Base(DeclarativeBase):
    """Declarative base class for SQLAlchemy models."""

    pass


def create_tables():
    """Tables creation"""
    Base.metadata.create_all(bind=engine)
