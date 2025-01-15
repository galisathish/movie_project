from .db_models import (
    Base,
    Movie,
    MovieCast,
    MovieDirector,
    MovieGenre,
    Genre,
    Cast,
    Director,
    Admin,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

mysql_connection_str = "mysql+mysqldb://satish:password@localhost/movie_db"
engine = create_engine(mysql_connection_str)


def create_tables():
    Base.metadata.create_all(engine)


def insert_movie(movie_name, year, overview, update):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()

    if isinstance(overview, str):
        overview = overview.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        if movie_name is not None or len(movie_name) != 0:

            movie = session.query(Movie).filter_by(movie_name=movie_name).first()

            if not movie:
                # Create a new movie instance
                new_movie = Movie(movie_name=movie_name, year=year, overview=overview)

                # Add the new movie to the session
                session.add(new_movie)

                # Commit the transaction
                session.commit()
                print("Movie inserted successfully!")

            elif update is True:

                if year is not None:
                    movie.year = year

                if overview is not None:
                    movie.overview = overview

                session.commit()
                print("Movie updated successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting movie: {e}")

    finally:
        # Close the session
        session.close()


def insert_genre(genre_id=None, genre_name=None):


    if isinstance(genre_name, str):
        genre_name = genre_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        if genre_name is not None or len(genre_name) != 0:

            genre = session.query(Genre).filter_by(genre_name=genre_name).first()

            if not genre:

                # Create a new genre instance
                new_genre = Genre(genre_id=genre_id, genre_name=genre_name)

                # Add the new genre to the session
                session.add(new_genre)

                # Commit the transaction
                session.commit()
                print("genre inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting genre: {e}")

    finally:
        # Close the session
        session.close()


def insert_director(director_id=None, director_name=None):

    if isinstance(director_name, str):
        director_name = director_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        if director_name is not None or len(director_name) != 0:

            director = (
                session.query(Director).filter_by(director_name=director_name).first()
            )

            if not director:

                # Create a new director instance
                new_director = Director(
                    director_id=director_id, director_name=director_name
                )

                # Add the new director to the session
                session.add(new_director)

                # Commit the transaction
                session.commit()
                print("director inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting director: {e}")

    finally:
        # Close the session
        session.close()


def insert_cast(cast_id=None, cast_name=None):

    if isinstance(cast_name, str):
        cast_name = cast_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        if cast_name is not None or len(cast_name) != 0:

            cast = session.query(Cast).filter_by(cast_name=cast_name).first()

            if not cast:

                # Create a new cast instance
                new_cast = Cast(cast_id=cast_id, cast_name=cast_name)

                # Add the new cast to the session
                session.add(new_cast)

                # Commit the transaction
                session.commit()
                print("cast inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting cast: {e}")

    finally:
        # Close the session
        session.close()


def insert_movie_genre(movie_name, genre_name):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()
    if isinstance(genre_name, str):
        genre_name = genre_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        movie = session.query(Movie).filter_by(movie_name=movie_name).first()
        if not movie:
            print("Movie not found")

        genre = session.query(Genre).filter_by(genre_name=genre_name).first()
        if not genre:
            print("Genre not found ")

        if movie and genre:

            # Create a new movie_genre instance
            new_movie_genre = MovieGenre(
                movie_id=movie.movie_id, genre_id=genre.genre_id
            )

            # Add the new movie_genre to the session
            session.add(new_movie_genre)

            # Commit the transaction
            session.commit()
            print("movie_genre inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting movie_genre: {e}")

    finally:
        # Close the session
        session.close()


def insert_movie_cast(movie_name, cast_name):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()

    if isinstance(cast_name, str):
        cast_name = cast_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        movie = session.query(Movie).filter_by(movie_name=movie_name).first()
        if not movie:
            print("Movie not found")

        cast = session.query(Cast).filter_by(cast_name=cast_name).first()
        if not cast:
            print("Cast not found ")

        if movie and cast:

            # Create a new movie_cast instance
            new_movie_cast = MovieCast(movie_id=movie.movie_id, cast_id=cast.cast_id)

            # Add the new movie_cast to the session
            session.add(new_movie_cast)

            # Commit the transaction
            session.commit()
            print("movie_cast inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting movie_cast: {e}")

    finally:
        # Close the session
        session.close()


def insert_movie_director(movie_name, director_name):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()

    if isinstance(director_name, str):
        director_name = director_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        movie = session.query(Movie).filter_by(movie_name=movie_name).first()
        if not movie:
            print("Movie not found")

        director = (
            session.query(Director).filter_by(director_name=director_name).first()
        )
        if not director:
            print("director not found")

        if movie and director:

            # Create a new movie_director instance
            new_movie_director = MovieDirector(
                movie_id=movie.movie_id, director_id=director.director_id
            )

            # Add the new movie_director to the session
            session.add(new_movie_director)

            # Commit the transaction
            session.commit()
            print("movie_director inserted successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting movie_director: {e}")

    finally:
        # Close the session
        session.close()


def delete_movie(movie_name=None):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the movie by its ID
        movie = session.query(Movie).filter_by(movie_name=movie_name).first()

        if movie:
            # Delete the movie from the session
            session.delete(movie)

            # Commit the transaction
            session.commit()
            print("Movie deleted successfully!")
        else:
            print("Movie not found!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error deleting movie: {e}")

    finally:
        # Close the session
        session.close()


def delete_cast(cast_name=None):

    if isinstance(cast_name, str):
        cast_name = cast_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the movie by its ID
        cast = session.query(Cast).filter_by(cast_name=cast_name).first()

        if cast:
            # Delete the movie from the session
            session.delete(cast)

            # Commit the transaction
            session.commit()
            print("cast deleted successfully!")
        else:
            print("cast not found!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error deleting cast: {e}")

    finally:
        # Close the session
        session.close()


def delete_director(director_name=None):

    if isinstance(director_name, str):
        director_name = director_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the movie by its ID
        director = (
            session.query(Director).filter_by(director_name=director_name).first()
        )

        if director:
            # Delete the movie from the session
            session.delete(director)

            # Commit the transaction
            session.commit()
            print("director deleted successfully!")
        else:
            print("director not found!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error deleting director: {e}")

    finally:
        # Close the session
        session.close()


def delete_genre(genre_name=None):

    if isinstance(genre_name, str):
        genre_name = genre_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the movie by its ID
        genre = session.query(Genre).filter_by(genre_name=genre_name).first()

        if genre:
            # Delete the movie from the session
            session.delete(genre)

            # Commit the transaction
            session.commit()
            print("genre deleted successfully!")
        else:
            print("genre not found!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error deleting genre: {e}")

    finally:
        # Close the session
        session.close()


def insert_admin(username, password, email, update):

    if isinstance(username, str):
        username = username.strip()

    if isinstance(passowrd, str):
        passowrd = passowrd.strip()

    if isinstance(email, str):
        email = email.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        if username is not None or len(username) != 0:

            admin = session.query(Admin).filter_by(username=username).first()

            if not admin:
                # Create a new movie instance
                new_admin = Admin(username=username, password=password, email=email)

                # Add the new movie to the session
                session.add(new_admin)

                # Commit the transaction
                session.commit()
                print("admin inserted successfully!")

            elif update is True:

                if password is not None:
                    admin.password = password

                if email is not None:
                    admin.email = email

                session.commit()
                print("admin updated successfully!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error inserting admin: {e}")

    finally:
        # Close the session
        session.close()


def delete_admin(username):

    if isinstance(username, str):
        username = username.strip()


    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the admin by its ID
        admin = session.query(Admin).filter_by(username=username).first()

        if admin:
            # Delete the admin from the session
            session.delete(admin)

            # Commit the transaction
            session.commit()
            print("Admin deleted successfully!")
        else:
            print("Admin not found!")

    except Exception as e:
        # Rollback the transaction if an error occurs
        session.rollback()
        print(f"Error deleting admin: {e}")

    finally:
        # Close the session
        session.close()


def get_movie_information(movie_name=None, movie_id=None):

    if isinstance(movie_name, str):
        movie_name = movie_name.strip()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    movie_info_dict = None

    try:

        query = (
            session.query(
                Movie.movie_name,
                Movie.year,
                Movie.overview,
                Director.director_name,
                Cast.cast_name,
                Genre.genre_name,
            )
            .outerjoin(MovieGenre, Movie.movie_id == MovieGenre.movie_id)
            .outerjoin(MovieDirector, Movie.movie_id == MovieDirector.movie_id)
            .outerjoin(MovieCast, Movie.movie_id == MovieCast.movie_id)
            .outerjoin(Cast, MovieCast.cast_id == Cast.cast_id)
            .outerjoin(Director, MovieDirector.director_id == Director.director_id)
            .outerjoin(Genre, MovieGenre.genre_id == Genre.genre_id)
        )

        if movie_name is not None:
            joined_info = query.filter(Movie.movie_name == movie_name).all()
        else:
            joined_info = query.filter(Movie.movie_id == movie_id).all()

        columns = ["movie_name", "year", "overview", "director", "cast", "genre"]
        df = pd.DataFrame(
            [{key: value for key, value in zip(columns, row)} for row in joined_info]
        )

        movie_info_dict = {
            "movie_name": df["movie_name"].unique().tolist()[0],
            "directors": df["director"].unique().tolist(),
            "cast": df["cast"].unique().tolist(),
            "genre": df["genre"].unique().tolist(),
            "year": df["year"].unique().tolist()[0],
            "overview": df["overview"].unique().tolist()[0],
        }

    except Exception as e:
        print(f"Error getting movie information: {e}")

    finally:
        # Close the session
        session.close()

    return movie_info_dict


def get_all_movies_by_year(year):

    Session = sessionmaker(bind=engine)
    session = Session()
    movies_by_year = []

    try:
        movies = (
            session.query(
                Movie.movie_name,
            )
            .filter(Movie.year == year)
            .all()
        )

        for movie_name in movies:
            movies_by_year.append(get_movie_information(movie_name=movie_name[0]))

    except Exception as e:
        print(e)
    finally:
        session.close()

    return movies_by_year


def get_all_movies_by_genre(genre_name):

    if isinstance(genre_name, str):
        genre_name = genre_name.strip()

    Session = sessionmaker(bind=engine)
    session = Session()

    movies_by_genre = []

    try:

        joined_info_list = (
            session.query(Genre.genre_id, MovieGenre.movie_id)
            .outerjoin(Genre, MovieGenre.genre_id == Genre.genre_id)
            .filter(Genre.genre_name == genre_name)
            .all()
        )

        if joined_info_list:

            movie_ids = set([joined_info.movie_id for joined_info in joined_info_list])

            for movie_id in movie_ids:
                movies_by_genre.append(get_movie_information(movie_id=movie_id))

    except Exception as e:
        print(e)
    finally:
        session.close()

    return movies_by_genre


def get_all_movies_by_director(director_name):

    if isinstance(director_name, str):
        director_name = director_name.strip()

    Session = sessionmaker(bind=engine)
    session = Session()

    movies_by_director = []

    try:

        joined_info_list = (
            session.query(Director.director_name, MovieDirector.movie_id)
            .outerjoin(Director, MovieDirector.director_id == Director.director_id)
            .filter(Director.director_name == director_name)
            .all()
        )

        if joined_info_list:

            movie_ids = set([joined_info.movie_id for joined_info in joined_info_list])

            for movie_id in movie_ids:
                movies_by_director.append(get_movie_information(movie_id=movie_id))

    except Exception as e:
        print(e)
    finally:
        session.close()

    return movies_by_director


def get_all_movies_by_cast(cast_name):

    if isinstance(cast_name, str):
        cast_name = cast_name.strip()

    Session = sessionmaker(bind=engine)
    session = Session()

    movies_by_cast = []

    try:

        joined_info_list = (
            session.query(Cast.cast_name, MovieCast.movie_id)
            .outerjoin(Cast, MovieCast.cast_id == Cast.cast_id)
            .filter(Cast.cast_name == cast_name)
            .all()
        )

        if joined_info_list:

            movie_ids = set([joined_info.movie_id for joined_info in joined_info_list])

            for movie_id in movie_ids:
                movies_by_cast.append(get_movie_information(movie_id=movie_id))

    except Exception as e:
        print(e)
    finally:
        session.close()

    return movies_by_cast


def add_movie_info(movie_name, overview, genre, cast, directors, year):

    insert_movie(movie_name, year, overview, update=True)

    for _genre in genre:

        insert_genre(genre_name=_genre)
        insert_movie_genre(movie_name, _genre)

    for _director in directors:
        insert_director(director_name=_director)
        insert_movie_director(movie_name, _director)

    for _cast in cast:
        insert_cast(cast_name=_cast)
        insert_movie_cast(movie_name, _cast)


def insert_movie_info_from_csv(csv_path):

    create_tables()

    movie_data = pd.read_csv(csv_path)
    columns = ["movie_name", "year", "genre", "overview", "director", "cast"]
    movie_data = movie_data[columns]
    movie_data["directors"] = movie_data["director"].str.split(",")
    movie_data["cast"] = movie_data["cast"].str.split(",")
    movie_data["genre"] = movie_data["genre"].str.split(",")
    movie_data = movie_data.dropna()
    movie_data = movie_data.drop(columns=["director"])

    for data in movie_data.to_dict(orient="records"):
        add_movie_info(**data)

    return movie_data


def get_movies_list():

    Session = sessionmaker(bind=engine)
    session = Session()

    movies_list = []

    try:
        movies_list = session.query(Movie.movie_name).all()
        if movies_list:
            movies_list = [movie_info[0] for movie_info in movies_list]

    except Exception as e:
        print(e)
    finally:
        session.close()

    return movies_list


def get_directors_list():

    Session = sessionmaker(bind=engine)
    session = Session()

    director_list = []

    try:
        director_list = session.query(Director.director_name).all()
        if director_list:
            director_list = [director_info[0] for director_info in director_list]

    except Exception as e:
        print(e)
    finally:
        session.close()

    return director_list


def get_genre_list():

    Session = sessionmaker(bind=engine)
    session = Session()

    genre_list = []

    try:
        genre_list = session.query(Genre.genre_name).all()
        if genre_list:
            genre_list = [genre_name[0] for genre_name in genre_list]

    except Exception as e:
        print(e)
    finally:
        session.close()

    return genre_list


def get_cast_list():

    Session = sessionmaker(bind=engine)
    session = Session()

    cast_list = []

    try:
        cast_list = session.query(Cast.cast_name).all()
        if cast_list:
            cast_list = [cast_name[0] for cast_name in cast_list]

    except Exception as e:
        print(e)
    finally:
        session.close()

    return cast_list
