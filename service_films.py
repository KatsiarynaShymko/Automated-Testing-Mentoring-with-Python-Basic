"""Coordinates repository operations"""

from database import Session
from film_models import Films
from repository_films import (add_film, delete_all_films, get_all_films,
                              update_film)


def main():
    """Coordinates operations on the films table."""

    def populate_films(session: Session) -> None:
        """Populates table with records"""
        films = [
            Films(title="Poor things", director="Yorgos Lanthimos", release_year=2023),
            Films(title="La la land", director="Damien Chazelle", release_year=2016),
            Films(
                title="Blade Runner 2049",
                director="Denis Villeneuve",
                release_year=2017,
            ),
        ]
        for film in films:
            add_film(session, film)

    with Session() as session:
        populate_films(session)
        films_before_update = get_all_films(session)

        print("Films before update".center(60, "*"))
        print(f"{'ID':<2} {'Title':<24} {'Director':<18} {'Year'}")
        print("-" * 60)
        for film in films_before_update:
            print(f"{film.id:<3}{film.title:<25}{film.director:<19}{film.release_year}")

        update_film(
            session,
            2,
            new_data={
                "title": "Kryshtal",
                "director": "Darya Zhuk",
                "release_year": 2018,
            },
        )

        print("Films after update".center(60, "*"))
        print(f"{'ID':<2} {'Title':<24} {'Director':<18} {'Year'}")
        print("-" * 60)
        for film in films_before_update:
            print(f"{film.id:<3}{film.title:<25}{film.director:<19}{film.release_year}")

        delete_all_films(session)

        films_after_deletion = get_all_films(session)
        if not films_after_deletion:
            print("\nAll records were deleted")
        else:
            for film in films_after_deletion:
                print(
                    f"{film.id}, Title: {film.title}, Director: {film.director}, Release year: {film.release_year}"
                )


if __name__ == "__main__":
    main()
