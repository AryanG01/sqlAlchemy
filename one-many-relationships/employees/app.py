from employeesModel import session, Employees as User


# Creating users
user_1 = User(username='Zeq Tech 1')
user_2 = User(username='Zeq Tech 2')
user_3 = User(username='Zeq Tech 3')

# Creating relationships between users
user_1.following.append(user_2)
user_2.following.append(user_3)

# Adding users to the session
session.add_all([user_1, user_2, user_3])
session.commit()

print(f"{user_1.following = }")
print(f"{user_2.following = }")
print(f"{user_3.following = }")
