from model import session, User, Post
from time import perf_counter

session.add_all(
    [
        User(
            name=f"User {i}",
            posts=[
                Post(
                    content=f"This is the lastest content for {z}",
                ) for z in range(5)
            ]
        ) for i in range(1_000)
    ]
)

session.commit()

print('\n Accessing all users posts')

users = session.query(User).all()

for user in users:
    print(user.name, user.posts)