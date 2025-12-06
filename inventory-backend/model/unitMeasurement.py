from config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class UnitMeasurement(Base):
    __tablename__ = "unit_measurement"

    abbreviation = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    # Back populates - connect with Specification
    specifications = relationship("Specification", back_populates="unit_measurement")