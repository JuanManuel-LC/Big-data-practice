# Archivo: app.py
# Un script simple para procesar datos

import json
from datetime import datetime

data = {
    "app": "Mi primera app con Docker",
    "timestamp": datetime.now().isoformat(),
    "python_version": "3.12",
    "message": "Si ves esto, tu Dockerfile funciona perfecto"
}

print(json.dumps(data, indent=2, ensure_ascii=False))