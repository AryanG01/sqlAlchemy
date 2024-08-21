from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

# Define the database URL for connecting to MySQL
mysql_db_url = "mysql+pymysql://root:Aryan1234@localhost:3306/aryandb2"

# Create an engine instance to manage the connection to the MySQL database
engine = create_engine(mysql_db_url, echo=False)

# Create a session factory bound to the engine for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define the User model
class Employees(Base):
    __tablename__ = 'employees'  # Name of the database table
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)  # Primary key column for the User model

    # Columns for username
    username = Column(String(100))

    # Relationship for self-referencing to represent users following other users
    following_id = Column(Integer, ForeignKey('employees.id'))  # Foreign key referencing another user
    following = relationship("Employees", remote_side=[id], uselist=True)  # Recursive relationship to the User model

    # Custom string representation of the User model
    def __repr__(self):
        return f"<Employee(id={self.id}, username={self.username}, following={self.following})>"

# Create all tables in the database using the defined models
Base.metadata.create_all(engine)
