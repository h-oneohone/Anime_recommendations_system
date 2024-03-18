from pydantic import BaseModel

# User Schemas
class UserBase(BaseModel):
    username: str
    gmail: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

# AnimeSeries Schemas
class AnimeSeriesBase(BaseModel):
    title: str
    image: str
    publisher: str
    description: str

class AnimeSeriesCreate(AnimeSeriesBase):
    pass

class AnimeSeries(AnimeSeriesBase):
    anime_id: int

    class Config:
        orm_mode = True

# Rating Schemas
class RatingBase(BaseModel):
    rating: int

class RatingCreate(RatingBase):
    user_id: int
    anime_id: int

class Rating(RatingBase):
    rating_id: int
    user_id: int
    anime_id: int

    class Config:
        orm_mode = True
