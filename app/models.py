from sqlalchemy import Column, Integer, String
from .database import Base


class CustomerDB(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)
    email= Column(String)
    status= Column(String)

