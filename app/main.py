from fastapi import FastAPI
from .routes import router
from .database import engine
from .models import Base 
from .auth_routes import auth_router


Base.metadata.create_all(bind=engine)
app= FastAPI()

app.include_router(router)
app.include_router(auth_router)

@app.get("/") 
def root(): 
    return {"message": "CRM API is live"} 

