from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Movement(Base):
    __tablename__ = "movement"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationship with AuditLog
    audit_movement = relationship("AuditLog", back_populates="movements")