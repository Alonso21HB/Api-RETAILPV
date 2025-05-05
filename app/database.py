from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

# Conexión a SQL Server con autenticación de Windows
#SQLALCHEMY_DATABASE_URL = (
    #"mssql+pyodbc://ALONSO/Devioz_bd?driver=ODBC+Driver+17+for+SQL+Server"
    #"mssql+pyodbc://localhost/Devioz_bd?driver=ODBC+Driver+17+for+SQL+Server"
    #"mssql+pyodbc://localhost@host.docker.internal:1433/Devioz_bd?driver=ODBC+Driver+17+for+SQL+Server"
#)
# Crear el motor
#engine = create_engine(
    #SQLALCHEMY_DATABASE_URL,
    #connect_args={"driver": "ODBC Driver 17 for SQL Server"}
#)

# Conexión a MySQL local
MYSQL_USER_LOCAL = "root"  # O el usuario que uses en tu MySQL
MYSQL_PASSWORD_LOCAL = "Alonso-123"  # La contraseña del usuario
MYSQL_HOST_LOCAL = "db"  # Cambia localhost si usas otro host o IP
MYSQL_PORT_LOCAL = "3306"  # Puerto de MySQL (generalmente es 3306)
MYSQL_DATABASE_LOCAL = "devioz_bd"  # Nombre de la base de datos

# Aquí definimos la URL de conexión de MySQL local
MYSQL_URL_LOCAL = f"mysql+mysqlconnector://{MYSQL_USER_LOCAL}:{MYSQL_PASSWORD_LOCAL}@{MYSQL_HOST_LOCAL}:{MYSQL_PORT_LOCAL}/{MYSQL_DATABASE_LOCAL}"

# Crear el motor para MySQL
engine_mysql_local = create_engine(MYSQL_URL_LOCAL, pool_recycle=3600)


# Conexión a MySQL (phpMyAdmin en Hostinger)
MYSQL_USER_HOSTINGER = "u777467137_deviozapp"
MYSQL_PASSWORD_HOSTINGER = "Deviozapp10+"
MYSQL_HOST_HOSTINGER = "auth-db465.hstgr.io"  # IP o dominio de la base de datos
MYSQL_PORT_HOSTINGER = "3306"  # Puerto de MySQL
MYSQL_DATABASE_HOSTINGER = "u777467137_deviozapp"

MYSQL_URL_HOSTINGER = f"mysql+mysqlconnector://{MYSQL_USER_HOSTINGER}:{MYSQL_PASSWORD_HOSTINGER}@{MYSQL_HOST_HOSTINGER}:{MYSQL_PORT_HOSTINGER}/{MYSQL_DATABASE_HOSTINGER}"

engine_mysql_hostinger = create_engine(MYSQL_URL_HOSTINGER, pool_recycle=3600)

# Crear la base
Base = declarative_base()

# Crear la sesión para MySQL local
SessionLocal_MySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_local)

# Crear la sesión para MySQL (phpMyAdmin)
SessionHostinger_MySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_hostinger)

# Función par
# a obtener la sesión local
def get_db_mysql_local():
    db = SessionLocal_MySQL()
    try:
        yield db
    finally:
        db.close()

# Función para obtener la sesión de MySQL (phpMyAdmin)
def get_db_mysql_hostinger():
    db = SessionHostinger_MySQL()
    try:
        yield db
    finally:
        db.close()



try:
    with engine_mysql_local.connect() as connection:
        print("Conexión exitosa a mysql local")
except Exception as e:
    print(f"Error al conectar a mysql local: {e}")

try:
    with engine_mysql_hostinger.connect() as connection:
        print("Conexión exitosa a MySQL (phpMyAdmin)")
except Exception as e:
    print(f"Error al conectar a MySQL (phpMyAdmin): {e}")