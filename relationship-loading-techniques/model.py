from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey, Text)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

db_url = "mysql+pymysql://root:Aryan1234@localhost:3306/day3"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    posts = relationship("Post", backref='user', lazy='joined')

    def __repr__(self):
        return f"<User(name={self.name})> "

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post(title={self.id})> "

Base.metadata.create_all(engine)