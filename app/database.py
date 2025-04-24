from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

# Conexión a SQL Server con autenticación de Windows
SQLALCHEMY_DATABASE_URL = (
    #"mssql+pyodbc://ALONSO/Devioz_bd?driver=ODBC+Driver+17+for+SQL+Server"
    "mssql+pyodbc://localhost/Devioz_bd?driver=ODBC+Driver+17+for+SQL+Server"
)
# Crear el motor
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"driver": "ODBC Driver 17 for SQL Server"}
)

# Conexión a MySQL (phpMyAdmin en Hostinger)
MYSQL_USER = "u777467137_deviozapp"
MYSQL_PASSWORD = "Deviozapp10+"
MYSQL_HOST = "auth-db465.hstgr.io"  # IP o dominio de la base de datos
MYSQL_PORT = "3306"  # Puerto de MySQL
MYSQL_DATABASE = "u777467137_deviozapp"

MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine_mysql = create_engine(MYSQL_URL, pool_recycle=3600)

# Crear la base
Base = declarative_base()

# Crear la sesión (SQLServer)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la sesión para MySQL (phpMyAdmin)
SessionLocal_MySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql)

# Función par
# a obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para obtener la sesión de MySQL (phpMyAdmin)
def get_db_mysql():
    db = SessionLocal_MySQL()
    try:
        yield db
    finally:
        db.close()



try:
    with engine.connect() as connection:
        print("Conexión exitosa a SQL Server")
except Exception as e:
    print(f"Error al conectar a SQL Server: {e}")

try:
    with engine_mysql.connect() as connection:
        print("Conexión exitosa a MySQL (phpMyAdmin)")
except Exception as e:
    print(f"Error al conectar a MySQL (phpMyAdmin): {e}")