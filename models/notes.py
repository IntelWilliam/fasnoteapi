from sqlalchemy import MetaData, Table
from config import engine, meta_data

notas = Table("notas", meta_data, autoload_with=engine, autoload=True)