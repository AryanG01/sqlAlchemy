import random

from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

names = ['John', 'Jane', 'Michael', 'Aryan', 'Jill', 'Jack', 'Sam', 'Tom', 'Jerry', 'Rick', 'Morty', 'Beth', 'Summer']
age = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

for x in range(20):
    user = User(name=random.choice(names), age=random.choice(age))
    session.add(user)

session.commit()