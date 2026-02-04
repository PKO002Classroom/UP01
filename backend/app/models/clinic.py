from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Clinic(Base):
    __tablename__ = 'clinics'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
    
    # Связь с докторами
    doctors = relationship('Doctor', back_populates='clinic')

