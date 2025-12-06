import bcrypt

# Hash password function
def hash_password(password: str) -> bytes:
    # Encode the password to bytes
    encoded_password = password.encode("utf-8")

    # Generate salt
    salt = bcrypt.gensalt()

    # Hash password with salt
    hashed_password = bcrypt.hashpw(encoded_password, salt)

    # Hash returned in bytes
    return hashed_password

# Verify password function
def verify_password(hashed_password: str, password: str) -> bool:
    try:
        # Encode the verification password
        encoded_password = password.encode("utf-8")

        encoded_hashed_password = hashed_password.encode("utf-8")

        # Compare verification password with hashed password
        return bcrypt.checkpw(encoded_password, encoded_hashed_password)
    except (ValueError, TypeError):
        return False