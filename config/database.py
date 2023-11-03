from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#conexion a la base de datos 
db_url = "mysql+pymysql://mastersan:mastersan05@sangtemplates.ckm0qy1jrhom.us-east-1.rds.amazonaws.com:3306/fasnote"
engine = create_engine(db_url)

# Definicion de METADATA
meta_data = MetaData()

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()



