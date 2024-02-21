from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)  # Specified length here
    password = Column(String(255))  # And here
    gmail = Column(String(255))  # And here

class AnimeSeries(Base):
    __tablename__ = "anime_series"
    anime_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specified length here
    image = Column(String(255))  # And here
    publisher = Column(String(255))  # And here
    description = Column(String(1024))  # Assuming descriptions might be longer

class Rating(Base):
    __tablename__ = "ratings"
    rating_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    anime_id = Column(Integer, ForeignKey('anime_series.anime_id'))
    rating = Column(Integer)
    user = relationship("User", back_populates="ratings")
    anime_series = relationship("AnimeSeries", back_populates="ratings")

User.ratings = relationship("Rating", order_by=Rating.rating_id, back_populates="user")
AnimeSeries.ratings = relationship("Rating", order_by=Rating.rating_id, back_populates="anime_series")
