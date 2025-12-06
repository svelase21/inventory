from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AppUser(Base):
    __tablename__ = "app_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Relationship many to one
    user_type_id = Column(Integer, ForeignKey("user_type.id"))

    # Relationship with AppUser
    user_type = relationship("UserType", back_populates="users")

    # Relationship with AuditLog
    audit_user = relationship("AuditLog", back_populates="users")