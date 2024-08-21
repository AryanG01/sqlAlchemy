import random

from sqlalchemy import and_

from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all users
users = session.query(User).where(and_(User.age >= 30, User.name == 'Michael')).all()

for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")