from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # Implement JWT token creation and return the token here
    return {"message": "Login successful (Implement JWT for actual login)"}

@app.post("/anime_series/")
def create_anime(anime: schemas.AnimeSeriesCreate, db: Session = Depends(get_db)):
    return crud.create_anime_series(db=db, anime=anime)

@app.get("/anime_series/{anime_id}", response_model=schemas.AnimeSeries)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    anime = crud.get_anime_series(db, anime_id=anime_id)
    if anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


