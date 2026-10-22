# Conectar a Redis desde Python (necesitas: pip install redis)

import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)
r.set('pipeline_status', 'ejecutando')
print(f"Estado del pipeline: {r.get('pipeline_status')}")