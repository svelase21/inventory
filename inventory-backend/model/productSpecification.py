from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class ProductSpecification(Base):
    __tablename__ = "product_specification"

    # --- Start - relations many to one ---
    product_code = Column(Integer, ForeignKey("product.code"), primary_key=True, nullable=False)
    specification_id = Column(Integer, ForeignKey("specification.id"), primary_key=True, nullable=False)
    # --- End - relations many to one ---

    ammount = Column(Integer, nullable=False)

    # --- Start Back populates - connect with entities ---
    product = relationship("Product", back_populates="specifications")
    specification = relationship("Specification", back_populates="products")
    # --- End Back populates - connect with entities ---