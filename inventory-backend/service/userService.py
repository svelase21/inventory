from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from schema.user import UserCreate, UserResponse
from repository import userRepository
from repository import userTypeRepository
from handler.registerHandler import handler_password
from util.auth import hash_password

class UserService:

    @staticmethod
    def create_new_user(db: Session, user: UserCreate) -> Response:

        # Get username if it exists
        db_user = userRepository.get_user_by_username(db, user.username)

        # Check if the username has been registered
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The username has been registered")
        
        # Check if the password is in the correct format
        handler_password(user.password)

        # hash password function
        hashed_password = hash_password(user.password)

        db_user_validate = UserCreate(
            username=user.username,
            password=hashed_password,
            user_type_id=user.user_type_id
        )
        
        return Response(
            content=userRepository.create_user(db, db_user_validate),
            status_code=status.HTTP_201_CREATED
        )
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> UserResponse:
        # Get username if it exists
        db_user = userRepository.get_user_by_username(db, username)

        # Check if the username has not been registered
        if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The username not found")
        
        # Get relationship
        type_user_name = userTypeRepository.find_user_type_by_id(db, db_user.user_type_id)

        # Check if the user type has not been registered
        if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user type not exists")
        
        db_user_reponse = UserResponse(
            id=db_user.id,
            username=db_user.username,
            user_type=type_user_name.name
        )
        
        return db_user_reponse