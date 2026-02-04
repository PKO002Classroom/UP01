from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    phone = Column(String)
    telegram_id = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    role = Column(String, default='patient')  # patient, doctor, admin

