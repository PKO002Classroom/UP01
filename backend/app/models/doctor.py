from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    specialty = Column(String, nullable=False)
    license_number = Column(String, unique=True)
    experience_years = Column(Integer)
    bio = Column(String)
    
    user = relationship('User')
    schedules = relationship('Schedule', back_populates='doctor')
    appointments = relationship('Appointment', back_populates='doctor')

