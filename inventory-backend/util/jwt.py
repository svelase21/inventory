from dotenv import load_dotenv
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from schema.token import TokenData

load_dotenv()

# Secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Algoritm
ALGORITHM = "HS256"

# Time of expiration token
ACCESS_TOKE_EXPIRE_MINUTES = 60

# Schema OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/auth/login")

# Create JWT token function
def create_access_token(data: dict):
    # Create new token JWT
    to_encode = data.copy()

    # Add expire time
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKE_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode token with secret key
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify JWT token function
def verify_token(token: str, credentials_exception: JWTError) -> TokenData:
    try:
        # Decode token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract username
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
        # Return data validated
        return TokenData(username=username)
    
    except JWTError:
        # When the token has expired or the credentials are incorrect
        raise credentials_exception
    
# Validate current user function
def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    # FastAPI: validation of token and return user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="The credentials could not be validated",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)