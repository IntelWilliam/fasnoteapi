from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from config.database import SessionLocal
from services.users import get_all_users

user = APIRouter()

@user.get('/usuarios')
def list_user(db:session = Depends(SessionLocal)):
  return get_all_users(db)

