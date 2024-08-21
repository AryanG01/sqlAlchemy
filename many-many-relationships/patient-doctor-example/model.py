from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey, Table, DateTime)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime

db_url = "mysql+pymysql://root:Aryan1234@localhost:3306/aryandb1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_date = Column(DateTime, default=datetime.now())
    notes = Column(String(50))

    doctor = relationship('Doctor', backref='appointments')
    patient = relationship('Patient', backref='appointments')


class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    specialty = Column(String(50))


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    dob = Column(DateTime)

Base.metadata.create_all(engine)