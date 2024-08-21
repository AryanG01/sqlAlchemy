from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# Query all users ordered by age in ascending order
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(user.name, user.age)

# Query all users ordered by age in descending order
users = session.query(User).order_by(User.age.desc()).all()

for user in users:
    print(user.name, user.age)