from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'mysql+pymysql://root:Aryan1234@localhost:3306/aryandb1'

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = relationship('Address', back_populates='user', uselist=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age})>"
    
class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f"<Address(id={self.id}, email={self.email})>"

Base.metadata.create_all(engine)