import json

# JSON tiene tipos nativos
datos = {
    "nombre": "Ana López",       # string
    "edad": 28,                  # number (entero)
    "saldo": 1523.45,            # number (decimal)
    "es_vip": True,              # boolean (true/false)
    "telefono": None,            # null (ausencia de dato)
    "direcciones": [             # array
        {"tipo": "casa", "ciudad": "Madrid"},
        {"tipo": "trabajo", "ciudad": "Toledo"}
    ]
}

# Serializar (Python dict → JSON string)
json_str = json.dumps(datos, ensure_ascii=False, indent=2)
print(json_str)

# Deserializar (JSON string → Python dict)
recuperado = json.loads(json_str)
print(f"\nTipo de edad: {type(recuperado['edad'])}")  # <class 'int'>
print(f"Tipo de es_vip: {type(recuperado['es_vip'])}")  # <class 'bool'>