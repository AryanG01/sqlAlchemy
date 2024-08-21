from datetime import datetime
from model import session, Patient, Doctor, Appointment

dr_smith = Doctor(name='Dr. Smith', specialty='Pediatrician')
john_doe = Patient(name='John Doe', dob=datetime(1990, 1, 1))
appointment = Appointment(doctor=dr_smith, patient=john_doe, notes='Physical Exam')

session.add_all([dr_smith, john_doe, appointment])
session.commit()

# Find all the appointments for Dr Smith
appointments_for_dr_smith = session.query(Appointment).filter(Appointment.doctor.has(name='Dr. Smith')).all()

print("Appointments for Dr. Smith:")
print(appointments_for_dr_smith)

# Find all the appointments for John Doe
appointments_for_john_doe = session.query(Appointment).filter(Appointment.patient.has(name='John Doe')).all()

print("Appointments for John Doe:")
print(appointments_for_john_doe)
