from service.userService import UserService
from fastapi import APIRouter, Depends
from schema.user import UserCreate
from sqlalchemy.orm import Session
from config.database import get_db


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_new_user(db, user)

