from fastapi import APIRouter, Depends, status
from fastapi import HTTPException
from src.dependency.database_dependency import get_db
from src.models import User
from sqlalchemy.orm import Session

user = APIRouter(prefix="/users",tags=["users"])

@user.get("")
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    if users:
        return users
    raise HTTPException(status.HTTP_404_NOT_FOUND,"users table is empty")

@user.get("/{id}")
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    """Return User by its own associated id"""
    user = db.query(User).filter(User.id == id).first()
    if user:
        return user
    raise HTTPException(status.HTTP_404_NOT_FOUND,"Could not find any user with the given id")

