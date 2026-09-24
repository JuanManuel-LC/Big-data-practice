import texto_utils as tu

nombre = "  Maria Lopez  "
print(tu.limpiar_nombre(nombre))

emails = ["ana@empresa.com",
        "ana@empresa.com",
        "ana.lopeze@empresa",
        "juanempresa"]

for email in emails:
    print(f"El email {email} tiene el formato correcto: {tu.validar_email(email)}")
    
