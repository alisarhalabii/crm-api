from fastapi import FastAPI
from .routes import router
from .database import engine
from .models import Base 

Base.metadata.create_all(bind=engine)
app= FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "CRM API is live"}