from service.authService import AuthService
from service.userService import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from schema.user import UserResponse, UserAuth
from schema.token import Token, TokenData
from sqlalchemy.orm import Session
from util.jwt import create_access_token, get_current_user
from config.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token)
def sign_in(
    user_auth: UserAuth,
    db: Session = Depends(get_db)
):
    # Sign in user and get data
    user_authenticated = AuthService.sign_in(db, user_auth)

    # Create JWT token
    access_token = create_access_token(
        data={"sub": user_authenticated.username}
    )

    # Return token
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def get_current_user(
        token_data: TokenData = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return UserService.get_user_by_username(db, token_data.username)