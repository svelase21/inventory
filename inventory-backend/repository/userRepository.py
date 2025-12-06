from sqlalchemy.orm import Session
from model import AppUser
from schema.user import UserCreate

# create function
def create_user(db: Session, user: UserCreate):
    db_user = AppUser(
        username=user.username,
        password=user.password,
        user_type_id=user.user_type_id
    )

    # Add object to session
    db.add(db_user)
    
    # Confirm changes into database
    db.commit()

    # Refresh object
    db.refresh(db_user)

    return "The user has been registered"

# --- start filter functions ---

def get_user_by_id(db: Session, user_id: int):
    return db.query(AppUser).filter(AppUser.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(AppUser).filter(AppUser.username == username).first()

# --- end filter functions ---