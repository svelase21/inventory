from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "product"

    code = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)

    # Relationship one to many
    category = Column(Integer, ForeignKey("category.id"))

    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    # Relationship with ProductCharacteristic
    characteristics = relationship("ProductCharacteristic", back_populates="product")

    # Relationship with ProductSpecification
    specifications = relationship("ProductSpecification", back_populates="product")

    # Relationship with ProductSpecification
    orders = relationship("OrderDetail", back_populates="product")