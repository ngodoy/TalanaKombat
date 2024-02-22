# Usa la imagen oficial de Python desde Docker Hub
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Usa CMD para aceptar argumentos al ejecutar el contenedor
CMD ["python", "main.py"]