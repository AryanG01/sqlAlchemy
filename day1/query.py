from sqlalchemy.orm import sessionmaker
from models import User, engine

# Create a session factory using the engine
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

# Query all users from the User table
users = session.query(User).all()

# Iterate over each user and print their id, name, and age
for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


# To query and want to obtain either one or no user
# Gives an error as there are multiple users
# users = session.query(User).one_or_none()
# print(users)

# filter_by() method to filter the query results
users = session.query(User).filter_by(age=30).all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


# updating values
user = session.query(User).filter_by(age=35).first()

if user:
    user.age = 30

session.commit()

# first() method to get the first result of the query
users = session.query(User).filter_by(age=30).all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


# delete values
user = session.query(User).filter_by(age=30).first()

session.delete(user)

session.commit()