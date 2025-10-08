"""CRUD operations"""

from typing import Sequence

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from film_models import Films


def add_film(session: Session, film: Films) -> None:
    """Add film into the table"""
    session.add(film)
    session.commit()


def get_all_films(session: Session) -> Sequence[Films]:
    """Find all films in the table"""
    return session.execute(select(Films)).scalars().all()


def update_film(session: Session, film_id: int, new_data: dict) -> None:
    """Update film"""
    film = session.get(Films, film_id)
    if film:
        for key, value in new_data.items():
            setattr(film, key, value)
        session.commit()


def delete_all_films(session: Session) -> None:
    """Delete all records in table"""
    session.execute(delete(Films))
    session.commit()
