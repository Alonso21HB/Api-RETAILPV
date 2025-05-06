# Usa una imagen base de Python
FROM python:3.9-slim

# Instalar dependencias necesarias para la compilación
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos al contenedor
COPY app/requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY app/ .

# Expone el puerto donde se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
