from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

reviews = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Review(BaseModel):
    movie_title: str
    liked : bool
    rating: Literal[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    comment: str | None = None

@app.post("/reviews")
def create_review(review: Review):
    reviews.append(review)
    return {
        "movie_title": review.movie_title,
        "liked": review.liked,
        "rating": review.rating,
        "comment": review.comment
    }


@app.get("/reviews")
def get_reviews():
    return reviews
            
