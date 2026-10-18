# Conectar a PostgreSQL desde Python (necesitas: pip install psycopg2-binary)

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="datos",
    password="secreto123",
    database="analytics"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
print(f"PostgreSQL: {cursor.fetchone()[0]}")
conn.clone()