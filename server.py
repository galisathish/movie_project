# uvicorn project:app --reload

from fastapi import FastAPI, Response
from .db_utilities import (
    insert_movie_info_from_csv,
    add_movie_info,
    get_movie_information,
    get_all_movies_by_cast,
    get_all_movies_by_director,
    get_all_movies_by_genre,
    get_all_movies_by_year,
    get_cast_list,
    get_directors_list,
    get_genre_list,
    get_movies_list,
)
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, model_validator
from typing import List, Optional
# from .main import *

app = FastAPI()  #instance

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/movies/movie/{movie_name}")
def get_movie_info(movie_name: str):
    return get_movie_information(movie_name=movie_name)


class MovieByGenre(BaseModel):

    genre_name: str
    return_n_movies: int = 10

    @model_validator(mode="before")
    def parse_a_obj(cls, data):
        return data


@app.post("/movies/genre_by_name")
def get_movie_info(movie_by_genre: MovieByGenre):
    return get_all_movies_by_genre(genre_name=movie_by_genre.genre_name)[
        : movie_by_genre.return_n_movies
    ]


class MovieByYear(BaseModel):

    year: int
    return_n_movies: int = 10

    @model_validator(mode="before")
    def parse_a_obj(cls, data):
        return data


@app.post("/movies/year")
def get_movie_info(movie_by_year: MovieByYear):
    return get_all_movies_by_year(year=movie_by_year.year)[
        : movie_by_year.return_n_movies
    ]


class MovieByCast(BaseModel):

    cast_name: str
    return_n_movies: int = 10

    @model_validator(mode="before")
    def parse_a_obj(cls, data):
        return data


@app.post("/movies/cast_by_name")
def get_movie_info(movie_by_cast: MovieByCast):
    return get_all_movies_by_cast(cast_name=movie_by_cast.cast_name)[
        : movie_by_cast.return_n_movies
    ]


class MovieByDirector(BaseModel):

    director_name: str
    return_n_movies: int = 10

    @model_validator(mode="before")
    def parse_a_obj(cls, data):
        return data

@app.post("/movies/director_by_name")
def get_movie_info(movie_by_director: MovieByDirector):
    return get_all_movies_by_director(director_name=movie_by_director.director_name)[
        : movie_by_director.return_n_movies
    ]

class MoviesInfo(BaseModel):

    movie_name: str
    year: int
    genre: List[str]
    overview: str
    directors: List[str]
    cast: List[str]

    @model_validator(mode="before")
    def parse_a_obj(cls, data):

        if isinstance(data["cast"], str):
            data["cast"] = data["cast"].split(",")

        if isinstance(data["directors"], str):
            data["directors"] = data["directors"].split(",")

        if isinstance(data["genre"], str):
            data["genre"] = data["genre"].split(",")

        return data

@app.post("/movies/add_movie")
def add_or_update_movie(movie_info: MoviesInfo):
    add_movie_info(**dict(movie_info))


@app.post("/movies/data_ingestion")
def data_ingest_from_csv():
    csv_path = "D:\project\project\data\Bollywood-Movie-Dataset\IMDB-Movie-Dataset(2023-1951).csv"
    insert_movie_info_from_csv(csv_path)


@app.get("/movies/movie")
def get_movies_name():
    return get_movies_list()


@app.get("/movies/cast")
def get_cast_name():
    return get_cast_list()


@app.get("/movies/genre")
def get_genre_name():
    return get_genre_list()


@app.get("/movies/director")
def get_director_name():
    return get_directors_list()

# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
#                                          detail="could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)


#     return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


# @app.get("/users/me/items")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": 1, "owner": current_user}]