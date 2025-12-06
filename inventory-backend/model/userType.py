from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class UserType(Base):
    __tablename__ = "user_type"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(50))

    # Relationship one to many
    users = relationship("AppUser", back_populates="user_type")