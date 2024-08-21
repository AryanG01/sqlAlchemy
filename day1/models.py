from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Define the database URL
mysql_db_url = "mysql+pymysql://root:Aryan1234@localhost:3306/aryandb1"

# Create an engine instance
engine = create_engine(mysql_db_url, echo=True)

# Create a base class for declarative models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# Create all tables defined by the models
Base.metadata.create_all(engine)
