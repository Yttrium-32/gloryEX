from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema.users import UserPublic, UserCreate, UserDelete
from app.schema.users import UserRequestDetails, UserVerifySuccess
from ..dependencies import get_db
from .. import crud

router = APIRouter()

@router.post("/users/create", response_model=UserPublic, tags=["users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    email_in_use = crud.get_user_by_email(db=db, email=user.email)
    username_in_use = crud.get_user_by_username(db=db, username=user.username)
    if email_in_use:
        raise HTTPException(status_code=400, detail="Email is already in use")
    if username_in_use:
        raise HTTPException(status_code=400, detail="Username is already in use")
    return crud.create_user(db=db, user=user)

@router.post("/users/verify", response_model=UserVerifySuccess, tags=["users"])
def verify_user_login(user: UserRequestDetails, db: Session = Depends(get_db)):
    is_verified = crud.verify_user_login(db=db, username=user.username, password=user.password)
    if is_verified:
        return is_verified
    else:
        raise HTTPException(status_code=400, detail="Incorrect password")

@router.get("/users/", response_model=list[UserPublic], tags=["users"])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

@router.delete("/users/delete", tags=["users"])
def delete_user(user: UserDelete, db: Session = Depends(get_db)):
    username_exists = crud.get_user_by_username(db=db, username=user.username)
    if not username_exists:
        raise HTTPException(status_code=400, detail="User does not exist")
    crud.delete_user(db=db, user=user)
    return {"detail": "User deleted successfully"}

