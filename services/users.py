from sqlalchemy.orm import Session
from models.users import usuarios

# defino mi funcion 
def get_all_users(db: Session) :
  return db.query(usuarios).all()

