from model import session, Student, Course

# math = Course(title='Math')
# english = Course(title='English')

# bill = Student(name='Bill', courses = [math, english])
# susan = Student(name='Susan', courses = [english])

# session.add_all([bill, susan, math, english])
# session.commit()

rob = session.query(Student).filter_by(name='Bill').first()

courses= [course.title for course in rob.courses]
print(courses)