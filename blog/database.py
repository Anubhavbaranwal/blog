from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
 

sqlalchemy_database_url = "sqlite:///./blog.db" 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(sqlalchemy_database_url,connect_args={"check_same_thread":False}) # Create a SQLite database
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) # Create a sessionmaker instance
Base = declarative_base() 

# Base is an instance of the DeclarativeMeta class, which is a class that is used to create classes that include the ORM functionality.






