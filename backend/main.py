from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from fastapi import File, UploadFile, Form
from base64 import b64encode
import shutil
import json
import os

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
    return {"message": "Login successful (Implement JWT for actual login)",
            "user": user.user_id}

@app.post("/anime_series/")
def create_anime(anime: schemas.AnimeSeriesCreate, db: Session = Depends(get_db)):
    # Save the file
    print("ok")
    return crud.create_anime_series(db=db, anime=anime)

@app.post("/create_anime/")
def create_anime(anime: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Parse the JSON string back to a Python dictionary
    anime_data = json.loads(anime)
    # Validate the parsed data with your Pydantic model
    anime_obj = schemas.AnimeSeriesCreate(**anime_data)

    # Save the file
    file_location = f"Images/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("file_location:",file_location)

    # Assuming the function 'create_anime_series' is adapted to accept 'anime_obj' and 'file_location'
    return crud.create_anime_series(db=db, anime=anime_obj, image_path=file_location)


@app.get("/anime_series/{anime_id}", response_model=schemas.AnimeSeries)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    anime = crud.get_anime_series(db, anime_id=anime_id)
    if anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime


@app.post("/upload_anime_image/{anime_id}")
async def upload_anime_image(anime_id: int, image: UploadFile = File(...), db: Session = Depends(get_db)):
    # Read the image file and encode it to base64
    image_content = await image.read()
    image_base64 = b64encode(image_content).decode('utf-8')

    # Call a CRUD operation to update the anime series with the image
    updated_anime = crud.update_anime_image(db=db, anime_id=anime_id, image_base64=image_base64)
    
    if updated_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    return {"message": "Image uploaded successfully", "anime_id": anime_id}


# @app.get("/anime_series/", response_model=List[schemas.AnimeSeries])
# def read_all_anime(db: Session = Depends(get_db)):
#     anime_series = crud.get_all_anime_series(db=db)
#     return anime_series

@app.get("/anime_series/", response_model=List[schemas.AnimeSeries])
def read_all_anime(db: Session = Depends(get_db)):
    anime_series = crud.get_all_anime_series(db=db)
    # Convert image paths to base64 for each anime series
    for anime in anime_series:
        if anime.image and os.path.isfile(anime.image):
            with open(anime.image, "rb") as image_file:
                encoded_image = b64encode(image_file.read()).decode('utf-8')
                anime.image = encoded_image
        else:
            # Handle cases where the image file does not exist
            anime.image = None  # Or set to a default image in base64 format
    return anime_series

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
