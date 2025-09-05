from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# replace with your own password if not 'admin123'
DATABASE_URL = "postgresql://postgres:admin123@localhost/crmdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
