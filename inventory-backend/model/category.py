from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(75), nullable=True)

    # Reference in the same table
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    # Children reference
    children = relationship("Category", backref=backref("parent", remote_side=[id]))
