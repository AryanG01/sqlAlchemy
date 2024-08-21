from models import session, User, Address

# new_user = User(name='Aryan1')
# new_address = Address(email='john1@example.com', user=new_user)
# session.add(new_user)
# session.add(new_address)
# session.commit()

# print(new_user.name)
# print(new_address.email)
# print(new_user.address.email)
# print(new_address.user.name)

user = session.query(User).filter_by(name='Aryan1').first()
print(f"User: {user.name}, Address: {user.address.email}")  
