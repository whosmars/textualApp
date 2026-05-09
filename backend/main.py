from fastapi import FastAPI
from uuid import UUID, uuid4
from models import User, Movie, Review


app = FastAPI()


#Temporal data, this data must be in a database

reviews = []
users = []
movies = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

#CREATE

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

#READ

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

#READ ALL

@app.get("/reviews")
def get_reviews():
    return reviews

@app.get("/users")
def get_user():
    return users

@app.get("/movies")
def get_movies():
    return movies

#UPDATE

@app.put("/review/{review_id}")
def update_review(review_id: UUID, updated_review : Review):
    for i,review in enumerate(reviews):
        if review_id == review.rewiew_id:
            updated_review.review_id = review_id
            reviews[i] = updated_review
            return {
                "message": "Review updated successfully",
                "review": updated_review
            }
    return {
        "message": "Review not found"
    }

@app.put("/movie/{movie_id}")
def update_movie(movie_id: UUID, updated_movie : Movie):
    for i,movie in enumerate(movies):
        if movie_id == movie.movie_id:
            updated_movie.movie_id = movie_id
            movies[i] = updated_movie
            return {
                "message": "Movie updated successfully",
                "review": updated_movie
            }
    return {
        "message": "Movie not found"
    }    

@app.put("/user/{user_id}")
def update_user(user_id: UUID, updated_user : User):
    for i,user in enumerate(users):
        if user_id == user.user_id:
            updated_user.user_id = user_id
            users[i] = updated_user
            return {
                "message": "User updated successfully",
                "review": updated_user
            }
    return {
        "message": "User not found"
    }     

#DELETE

@app.delete("/review/{review_id}")
def delete_review(review_id: UUID):
    for index, review in enumerate(reviews):
        if review.review_id == review_id:
            deleted_review = reviews.pop(index)

            return {
                "message": "Review deleted successfully",
                "deleted_review": deleted_review
            }

    return {
        "message": "Review not found"
    }

@app.delete("/user/{user_id}")
def delete_user(user_id: UUID):
    for index, user in enumerate(users):
        if user.user_id == user_id:
            deleted_user = users.pop(index)

            return {
                "message": "User deleted successfully",
                "deleted_user": deleted_user
            }

    return {
        "message": "User not found"
    }

@app.delete("/movie/{movie_id}")
def delete_movie(movie_id: UUID):
    for index, movie in enumerate(movies):
        if movie.movie_id == movie_id:
            deleted_movie = movies.pop(index)

            return {
                "message": "Movie deleted successfully",
                "deleted_movie": deleted_movie
            }

    return {
        "message": "Movie not found"
    }