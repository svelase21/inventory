from sqlalchemy.orm import Session
from model import UserType
from schema.userType import UserTypeBase

# Create function
def create_user_type(db: Session, user_type: UserTypeBase):
    db_user_type = UserType(
        id=user_type.id,
        name=user_type.name,
        description=user_type.description
    )

    # Add object to session
    db.add(db_user_type)
    
    # Confirm changes into database
    db.commit()

    return "Created user type"

# Read funcion
def find_user_type_by_id(db: Session, user_type_id: int):
    return db.query(UserType).filter(UserType.id == user_type_id).first()