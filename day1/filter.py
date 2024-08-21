from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# Qquery all users
users = session.query(User).all()

print(f"Total number of users: {len(users)}")

# Query all users filtered by age >= 50
users = session.query(User).filter(User.age >= 50).all()

print(f"Users with age >= 50: {len(users)}")

# Query all users filtered by age >= 50 and name == 'Aryan'
users = session.query(User).filter(User.age >= 50, User.name == 'Aryan').all()

print(f"Users with age >= 50 and name == 'Aryan': {len(users)}")