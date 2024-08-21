from sqlalchemy import (Column, Integer, String, create_engine, ForeignKey, Table)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

db_url = "mysql+pymysql://root:Aryan1234@localhost:3306/aryandb1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_course'

    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column("course_id", Integer, ForeignKey('courses.id'))

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship('Course', secondary='student_course', back_populates='students')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    students = relationship('Student', secondary='student_course', back_populates='courses')

Base.metadata.create_all(engine)