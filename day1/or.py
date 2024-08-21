import random

from sqlalchemy import or_

from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all users
users = session.query(User).where(or_(User.age >= 30, User.name == 'Michael')).all()

for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")