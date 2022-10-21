from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.environ.get("DATABASE_URL"))
Session = sessionmaker(bind=engine)
Base = declarative_base()

