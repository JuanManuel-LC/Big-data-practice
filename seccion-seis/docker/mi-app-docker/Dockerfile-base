# Archivo: Dockerfile (sin extension, exactamente ese nombres)
FROM python:3.12-slim

WORKDIR /app

#Primero copiamos SOLO requirements.txt (truco cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Luego copiamos el codigo
COPY . .

CMD ["python", "app.py"]