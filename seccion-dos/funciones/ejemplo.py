def tiene_arroba(email):
    return "@" in email

def tiene_punto(email):
    return "." in email

def es_email_valido(email):
    return tiene_arroba(email) and tiene_punto(email)

print(es_email_valido("ana@gmail.com"))
print(es_email_valido("ana_sin_arroba"))