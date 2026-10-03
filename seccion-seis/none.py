# None es "aqui no hay nada", y no es lo mismo que ""

email_a = None      # no tenemos el dato
email_b = ""        # tenemos el dato y esta vacio

print(email_a is None)      # True <--- Para None se compara con is
print(email_b is None)      # False
print(email_b == "")        # True

# Y el indice -1: el ultimo contando desde el final
lecturas = [4.2, 4.5, 5.1, 9.1]
print(lecturas[-1])         # 9.1 <-- el ultimo, sin saber cuantos hay