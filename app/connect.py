from sqlalchemy import create_engine, Column, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_LOCALHOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_LOCALHOST}:3306/{DB_NAME}"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



