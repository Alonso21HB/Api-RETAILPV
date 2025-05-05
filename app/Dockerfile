# Usar una imagen base con Python
FROM python:3.9-slim



# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias necesarias para compilar pyodbc
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

RUN pip install --upgrade pip

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Copiar el código de la aplicación al contenedor
COPY . .

# Exponer el puerto 8000 para la API
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
