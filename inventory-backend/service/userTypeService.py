from repository import userTypeRepository
from sqlalchemy.orm import Session
from schema.userType import UserTypeBase
from fastapi import Response, status

class UserTypeService:

    @staticmethod
    def create_new_user_type(db: Session, user_type: UserTypeBase) -> Response:
        return Response(
            content=userTypeRepository.create_user_type(db, user_type),
            status_code=status.HTTP_201_CREATED
        )