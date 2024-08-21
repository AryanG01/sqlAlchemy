import random

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# group users by age
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()

print(users)