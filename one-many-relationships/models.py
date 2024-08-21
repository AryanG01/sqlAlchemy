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

# Define a base model with an `id` column as the primary key
class BaseModel(Base):
    __abstract__ = True  # This class won't be mapped to a database table directly
    __allow_unmapped__ = True  # Allows models that inherit from BaseModel to be partially unmapped

    id = Column(Integer, primary_key=True)  # Primary key column for all models

# Define the Addresss model
class Addresss(BaseModel):
    __tablename__ = 'address'  # Name of the database table

    # Columns for city, state, and zip_code
    city = Column(String(100))
    state = Column(String(100))
    zip_code = Column(Integer)

    # ForeignKey to establish a relationship with the 'users' table
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # Relationship to the User model, creating a bidirectional relationship
    user: Mapped["User"] = relationship(back_populates="address")

    # Custom string representation of the Addresss model
    def __repr__(self):
        return f"Address(id={self.id}, city={self.city}, state={self.state}, zip_code={self.zip_code}, user_id={self.user_id})"

# Define the User model
class User(BaseModel):
    __tablename__ = 'users'  # Name of the database table

    # Columns for name and age
    name = Column(String(100))
    age = Column(Integer)

    # Relationship to the Addresss model, indicating a user can have multiple addresses
    address: Mapped[list["Addresss"]] = relationship(back_populates="user")

    # Custom string representation of the User model
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age})"

# Create all tables in the database using the defined models
Base.metadata.create_all(engine)
