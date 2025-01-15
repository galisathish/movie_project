from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True,  autoincrement=True)
    movie_name = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    overview = Column(Text)
    
class Genre(Base):
    __tablename__ = 'genres'

    genre_id = Column(Integer, primary_key=True,  autoincrement=True)
    genre_name = Column(String(255), nullable=False)

class Director(Base):
    __tablename__ = 'directors'

    director_id = Column(Integer, primary_key=True,  autoincrement=True)
    director_name = Column(String(255), nullable=False)

class Cast(Base):
    __tablename__ = 'casts'

    cast_id = Column(Integer, primary_key=True,  autoincrement=True)
    cast_name = Column(String(255), nullable=False)

class MovieGenre(Base):
    __tablename__ = 'movie_genres'

    movie_id = Column(Integer, ForeignKey('movies.movie_id',ondelete="CASCADE"), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.genre_id',ondelete="CASCADE"), primary_key=True)

class MovieCast(Base):
    __tablename__ = 'movie_casts'

    movie_id = Column(Integer, ForeignKey('movies.movie_id',ondelete="CASCADE"), primary_key=True)
    cast_id = Column(Integer, ForeignKey('casts.cast_id',ondelete="CASCADE"), primary_key=True)

class MovieDirector(Base):
    __tablename__ = 'movie_directors'

    movie_id = Column(Integer, ForeignKey('movies.movie_id',ondelete="CASCADE"), primary_key=True)
    director_id = Column(Integer, ForeignKey('directors.director_id',ondelete="CASCADE"), primary_key=True)

class MovieDBAdmin(Base):
    __tablename__ = 'movie_db_admin'

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

