from sqlalchemy import MetaData, Table
from config.database import engine, meta_data

meta_data.reflect(bind=engine)

usuarios = meta_data.tables['usuarios']

