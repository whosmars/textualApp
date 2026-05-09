from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from uuid import UUID, uuid4

app = FastAPI()

reviews = []
users = []
movies = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Review(BaseModel):
    review_id : UUID = Field(default_factory=uuid4)
    liked : bool | None = None
    rating: Literal[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    comment: str | None = None
    movie_id : UUID
    who_made_the_review : UUID

class Movie(BaseModel):
    movie_id : UUID = Field(default_factory=uuid4)
    genre : Literal ["Thriller", "Suspense", "Horror", "Drama", "Comedy"] | None = None
    movie_title : str
    director : str | None = None
    year : int | None = None
    img: str | None = None


class User(BaseModel):
    user_id : UUID = Field(default_factory=uuid4)
    username : str
    total_reviews : int = 0


@app.get("/user/{user_id}")
def get_user_by_id (user_id : UUID):
    for user in users:
        if user.user_id == user_id:
            return {
                "message": "User Found Succesfully",
                "user_by_id" : user
            }
    return {
        "message": "User Not Found",
    }

@app.get("/review/{review_id}")
def get_reviews_by_id (review_id : UUID):
    for review in reviews:
        if review.review_id == review_id:
            return {
                "message": "Review Found Succesfully",
                "review_by_id" : review
            }
    return {
        "message": "Review Not Found",
    }

@app.get("/movie/{movie_id}")
def get_movies_by_id (movie_id : UUID):
    for movie in movies:
        if movie.movie_id == movie_id:
            return {
                "message": "Movie Found Succesfully",
                "movie_by_id" : movie
            }
    return {
        "message": "Movie Not Found",
    }

@app.post("/review")
def create_review(review: Review):
    reviews.append(review)
    return {
        "message": "Review created successfully",
        "Object": review
    }

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {
        "message": "User created successfully",
        "Object": user
    }

@app.post("/movie")
def create_movie(movie : Movie):
    movies.append(movie)
    return {
        "message": "Movie created successfully",
        "Object": movie
    }


@app.get("/reviews")
def get_reviews():
    return reviews

@app.get("/users")
def get_user():
    return users

@app.get("/movies")
def get_movies():
    return movies
            
