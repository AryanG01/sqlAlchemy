
from models import Addresss, session, User

# Creating users
user_1 = User(name='John Doe', age=52)
user_2 = User(name='Jane Smith', age=34)

# Creating addresses
address_1 = Addresss(city='New York', state='NY', zip_code=10001)
address_2 = Addresss(city='Los Angeles', state='CA', zip_code=90001)
address_3 = Addresss(city='Chicago', state='IL', zip_code=60007)

# Assigning addresses to users
user_1.address.extend([address_1, address_2])
user_2.address.append(address_3)

# Adding users to the session
session.add(user_1)
session.add(user_2)

# Commit the session to persist the new user
session.commit()


print(f"User 1 Address: {user_1.address}")
print(f"User 2 Address: {user_2.address}")
print(f"Address 1 User: {address_1.user}")