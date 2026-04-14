from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


#DATABASE_URL= "postgresql://postgres:Appelsinstjerna_2026@localhost:5432/crm_db"
DATABASE_URL= os.getenv("DATABASE_URL")
engine= create_engine(DATABASE_URL)

SessionLocal= sessionmaker(bind=engine)
Base= declarative_base()