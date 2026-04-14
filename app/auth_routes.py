from fastapi import APIRouter, HTTPException
from .models import UserDB
from .database import SessionLocal
from .auth import hash_password, verify_password, create_access_token
from pydantic import BaseModel

auth_router= APIRouter(prefix="/auth")

class User(BaseModel):
    username: str
    password: str


@auth_router.post("/register")
def register(user: User):
    db = SessionLocal()
    hashed = hash_password(user.password)

    db_user= UserDB(username=user.username, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()

    return{"message": "User created"}


@auth_router.post("/login")
def login(user: User):
    db= SessionLocal()
    db_user= db.query(UserDB).filter(UserDB.username== user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        db.close()
        raise HTTPException(status_code= 401, detail= "Invalid credentials")
    
    token= create_access_token({"sub": db_user.username})
    db.close()
    return {"acess_token": token, "token_type": "bearer"}

