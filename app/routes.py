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

@router.put("/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    db= SessionLocal()
    db_customer= db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if not db_customer:
        db.close()
        return {"error": "Customer not found"}
    # update feilds
    db_customer.name= customer.name
    db_customer.email = customer.email
    db_customer.status= customer.status

    db.commit()
    db.refresh(db_customer)
    db.close()

    return db_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    db = SessionLocal()
    db_customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    
    if not db_customer:
        db.close()
        return {"error": "Customer not found in database"}
     
    db.delete(db_customer) 
    db.commit() 
    db.close() 

    return{"Message": "Customer deleted from database"} 