from typing import Literal
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


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