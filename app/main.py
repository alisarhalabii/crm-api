from fastapi import FastAPI
from .routes import router
from .database import engine
from .models import Base 
from .auth_routes import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(router)
app.include_router(auth_router)

# Root
@app.get("/") 
def root(): 
    return {"message": "CRM API is live"}