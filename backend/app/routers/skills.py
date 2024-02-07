from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile  # for image uploads
from sqlalchemy.orm import Session
from uuid import uuid4 as gen_unique_name
from pathlib import Path

from app.schema.skills import SkillCreate, SkillPublic
from app.dependencies import get_db
from app import crud

# Check if static images file path exits, if not create it
IMAGE_FILE_PATH = Path("static/images/")
IMAGE_FILE_PATH.mkdir(parents=True, exist_ok=True)

router = APIRouter()

@router.post("/users/{user_id}/skills/", response_model=SkillPublic, tags=["skills"])
def create_skill_for_user_using_id(
        user_id: int, 
        skill: SkillCreate, 
        db: Session = Depends(get_db)
    ):
    user_exists = crud.get_user_by_id(db=db, user_id=user_id)
    if user_exists:
        return crud.create_user_skill(db=db, skill=skill, user_id=user_id)
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

@router.post("/users/{user_id}/skills_image", tags=["skills"])
def create_skill_for_user_using_id_wimage(
        user_id: int, 
        image_upload: UploadFile = File(...), 
        skill: SkillCreate = Depends(), 
        db: Session = Depends(get_db)
    ):
    if not image_upload:
        return {"detail": "No upload file sent"}

    user_exists = crud.get_user_by_id(db=db, user_id=user_id)
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist")

    filename = image_upload.filename
    extention = filename.split(".")[1]
    gen_name = str(IMAGE_FILE_PATH) + "/" + str(gen_unique_name()) + "." + extention
    file_content = image_upload.file.read()
    with open(gen_name, "wb+") as image:
        image.write(file_content)

    return crud.create_user_skill(db=db, skill=skill, user_id=user_id, cert_image_path=gen_name)

@router.get("/users/{user_id}/get_skill", response_model=list[SkillPublic], tags=["skills"])
def get_skill_by_user_id(user_id: int, db: Session = Depends(get_db)):
    skills = crud.get_skills_by_user_id(db=db, user_id=user_id)
    return skills

