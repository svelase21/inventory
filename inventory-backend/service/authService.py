from schema.user import UserAuth, UserResponse
from repository import userRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from util.auth import verify_password

class AuthService:
    # Sign in method
    @staticmethod
    def sign_in(db: Session, user_auth: UserAuth) -> UserResponse:
        db_user = userRepository.get_user_by_username(db, user_auth.username)

        # Check if the username has been registered
        if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username not found")
        
        hashed_password = db_user.password
        
        if verify_password(hashed_password, user_auth.password):
            return db_user
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad credentials")