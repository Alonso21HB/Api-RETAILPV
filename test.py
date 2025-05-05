import sys
import os
from sqlalchemy.orm import Session

# Agregar la carpeta app al path de importación
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from database import engine_mysql_local  # Ahora puede importar correctamente
from models import Categoria  # Asegúrate de que 'Cliente' sea el modelo adecuado

# Función para verificar si hay datos en la tabla
def verificar_datos_en_tabla():
    try:
        # Crear una sesión
        session = Session(bind=engine_mysql_local)
        
        # Consultar si hay datos en la tabla 'Cliente'
        cliente_count = session.query(Categoria).count()  # Contar los registros en la tabla Cliente

        # Verificar si la tabla tiene registros
        if cliente_count > 0:
            print(f"Hay {cliente_count} registros en la tabla 'Categoria'.")
        else:
            print("La tabla 'Categoria' está vacía.")
        
        # Cerrar la sesión
        session.close()

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Ejecutar la función
verificar_datos_en_tabla()

