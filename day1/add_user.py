from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

#After already executing these statemnts i commented them out to avoid duplicates
# Create a new user
# new_user = User(name='Aryan', age=23)

# Add the new user to the session
# session.add(new_user)

user_1 = User(name='John', age=30)
user_2 = User(name='Jane', age=25)
user_3 = User(name='Michael', age=35)

session.add(user_1)
session.add_all([user_2, user_3])

# Commit the session to persist the new user
session.commit()