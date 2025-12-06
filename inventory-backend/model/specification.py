from config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Specification(Base):
    __tablename__ = "specification"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    type = Column(String, nullable=False)

    # Relationship many to one
    um = Column(String, ForeignKey("unit_measurement.abbreviation"), nullable=True)

    # Back populates - connect with UnitMeasurement
    unit_measurement = relationship("UnitMeasurement", back_populates="specifications")

    # Back populates - connect with ProductSpecification
    products = relationship("ProductSpecification", back_populates="specification")