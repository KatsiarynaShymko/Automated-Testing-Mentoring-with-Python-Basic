from setting_up_the_database import Films, Session, create_tables

create_tables()

session = Session()

film1 = Films(title='Poor things', director='Yorgos Lanthimos', release_year=2023)
film2 = Films(title='La la land', director='Damien Chazelle', release_year=2016)
film3 = Films(title='Blade Runner 2049', director='Denis Villeneuve', release_year=2017)

session.add_all([film1, film2, film3])
session.commit()

films_before_update = session.query(Films).all()

print('Films before update'.center(60, '*'))
print(f"{'ID':<2} {'Title':<24} {'Director':<18} {'Year'}")
print("-" * 60)
for film in films_before_update:
    print(f"{film.id:<3}{film.title:<25}{film.director:<19}{film.release_year}")

film_update = session.get(Films, 2)

if film_update:
    film_update.title = 'Kryshtal'
    film_update.director = 'Darya Zhuk'
    film_update.release_year = 2018
    session.commit()

films = session.query(Films).all()

print('Films after update'.center(60, '*'))
print(f"\n{'ID':<2} {'Title':<24} {'Director':<18} {'Year'}")
print("-" * 60)
for film in films:
    print(f"{film.id:<3}{film.title:<25}{film.director:<19}{film.release_year}")

session.query(Films).delete()
session.commit()

films_after_deletion = session.query(Films).all()
if not films_after_deletion:
    print("\nAll records were deleted")
else:
    for film in films_after_deletion:
        print(f"{film.id}, Title: {film.title}, Director: {film.director}, Release year: {film.release_year}")

session.close()

