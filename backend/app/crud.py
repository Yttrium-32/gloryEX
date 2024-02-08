from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from . import models
from .schema import users, skills

hasher = PasswordHasher()

def create_user(*, db: Session, user: users.UserCreate):
    hashed_password = hasher.hash(user.password)
    db_user = models.Users(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(*, db: Session, user: users.UserDelete):
    db_user = db.query(models.Users).filter(models.Users.username == user.username).first()
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)

def create_user_skill(*, db: Session, skill: skills.SkillCreate, user_id: int, cert_image_path: str = None):
    db_skill = models.Skills(**skill.model_dump(), user_id=user_id, certificate_image_path=cert_image_path)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def verify_user_login(*, db: Session, username: str, password: str):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    hashed_password = user.password

    try:
        hasher.verify(hashed_password, password)
    except VerifyMismatchError:
        return False

    return user

def get_skills_by_user_id(*, db: Session, user_id: int):
    return db.query(models.Skills).filter(models.Skills.user_id == user_id).all()

def get_users(*, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()

def get_user_by_username(*, db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def get_user_by_email(*, db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()

def get_user_by_id(*, db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def get_user_id(*, db: Session, username: str):
    user = db.query(models.Users).filter(models.Users).filter_by(username == username).first()
    user_id: int = user.id
    return user_id

