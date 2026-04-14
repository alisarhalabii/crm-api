from fastapi import APIRouter
from .models import CustomerDB
from .database import SessionLocal
from pydantic import BaseModel


router = APIRouter(prefix="/customers")

class Customer(BaseModel):
    name: str
    email: str
    status: str #leads, in contact, customer

@router.post("/")
def create_customer(customer: Customer):
    database= SessionLocal()
    db_customer= CustomerDB(**customer.model_dump()) #model_dump() instead of dict() because dict is deprecated
    database.add(db_customer)
    database.commit()
    database.refresh(db_customer)
    database.close()
    return db_customer


@router.get("/")
def get_customers():
    db= SessionLocal()
    customers = db.query(CustomerDB).all()
    db.close()
    return customers
   #return {"message": "HELLO ALISAR"} --> Testing respons for direct get function in fastapi


