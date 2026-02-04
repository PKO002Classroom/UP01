from fastapi import APIRouter
from app.api.v1.endpoints import users, doctors, appointments

api_router = APIRouter()

api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['doctors'])
api_router.include_router(appointments.router, prefix='/appointments', tags=['appointments'])

