#Etapa 1: construir (con herramientas pesadas)
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/build/deps -r requirements.txt

#Etapa 2: ejecutar (sin herramientas de build)
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /build/deps /usr/local/lib/python3.12/site-packages/
COPY . .
CMD ["python", "app.py"]