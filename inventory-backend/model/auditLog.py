from config.database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True, index=True)

    # ------- Start to relationship many to one -------
    movement_id = Column(Integer, ForeignKey("movement.id"))
    user_id = Column(Integer, ForeignKey("app_user.id"))
    # ------- End to relationship many to one -------

    audit_date = Column(DateTime, nullable=False)

    # Relationship with Movement
    movements = relationship("Movement", back_populates="audit_movement")

    # Relationship with AppUser
    users = relationship("AppUser", back_populates="audit_user")
