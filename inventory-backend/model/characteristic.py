from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Characteristic(Base):
    __tablename__ = "characteristic"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationship with ProductCharacteristic
    products = relationship("ProductCharacteristic", back_populates="characteristic")

