# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY main.py .
COPY websocket_server.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que escucha tu servidor
EXPOSE 5000

# Ejecuta el archivo principal cuando el contenedor se inicie
CMD ["python", "main.py"]
