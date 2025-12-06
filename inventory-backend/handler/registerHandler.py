from fastapi import HTTPException, status

def handler_password(password: str):
    # Length validation
    if len(password) < 8:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The password must have a minimum of 8 characters")
    if len(password) > 32:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The password must have a maximum of 32 characters")
    
    # Lowercase validation
    if not any(c.islower() for c in password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The password must contain at least one lowercase character")
    
    # Uppercase validation
    if not any(c.isupper() for c in password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The password must contain at least one uppercase character")
    
    # Alphanumeric validation
    if not any(not c.isalnum() for c in password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The password must contain at least one special character")