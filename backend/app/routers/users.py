from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema.users import UserPublic, UserCreate, UserRequestDetails
from ..dependencies import get_db
from .. import crud

router = APIRouter()

@router.post("/users/", response_model=UserPublic, tags=["users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    email_in_use = crud.get_user_by_email(db=db, email=user.email)
    username_in_use = crud.get_user_by_username(db=db, username=user.username)
    if email_in_use:
        raise HTTPException(status_code=400, detail="Email is already in use")
    if username_in_use:
        raise HTTPException(status_code=400, detail="Username is already in use")
    return crud.create_user(db=db, user=user)

@router.post("/users/verify", tags=["users"])
def verify_user_login(user: UserRequestDetails, db: Session = Depends(get_db)):
    is_verified = crud.verify_user_login(db=db, username=user.username, password=user.password)
    if is_verified:
        return {"detail": "Login success"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect password")

