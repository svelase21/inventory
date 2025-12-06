from service.userTypeService import UserTypeService
from fastapi import APIRouter, Depends
from schema.userType import UserTypeBase
from sqlalchemy.orm import Session
from config.database import get_db

router = APIRouter(prefix="/user-types", tags=["User types"])

@router.post("/")
def create_new_user_type(
    user_type: UserTypeBase,
    db: Session = Depends(get_db)
):
    return UserTypeService.create_new_user_type(db, user_type)