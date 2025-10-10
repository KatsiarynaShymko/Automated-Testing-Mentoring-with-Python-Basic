"""Database schema for the Films table."""

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Films(Base):
    """ORM model representing a film record in the database."""

    __tablename__ = "films"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    director: Mapped[str] = mapped_column(String(120), nullable=False)
    release_year: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Film(id={self.id}, title={self.title!r}, director={self.director!r}, year={self.release_year}"
