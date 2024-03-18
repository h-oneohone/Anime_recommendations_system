from sqlalchemy.orm import Session
from models import User, AnimeSeries
from werkzeug.security import generate_password_hash, check_password_hash
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = generate_password_hash(user.password)
    db_user = User(username=user.username, password=hashed_password, gmail=user.gmail)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and check_password_hash(user.password, password):
        return user
    return False

def create_anime_series(db: Session, anime: schemas.AnimeSeriesCreate, image_path: str):
    print(anime.dict())
    print("image_path:")
          
    db_anime = AnimeSeries(**anime.dict())
    db_anime.image = image_path
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

def update_anime_image(db: Session, anime_id: int, image_base64: str):
    db_anime = db.query(AnimeSeries).filter(AnimeSeries.anime_id == anime_id).first()
    if db_anime:
        db_anime.image = image_base64
        db.commit()
        db.refresh(db_anime)
        return db_anime
    return None


def get_anime_series(db: Session, anime_id: int):
    return db.query(AnimeSeries).filter(AnimeSeries.anime_id == anime_id).first()

def get_all_anime_series(db: Session):
    return db.query(AnimeSeries).all()

