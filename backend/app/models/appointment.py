from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('users.id'))
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default='scheduled')  # scheduled, completed, cancelled, no-show
    notes = Column(String)
    
    doctor = relationship('Doctor', back_populates='appointments')
    patient = relationship('User')

