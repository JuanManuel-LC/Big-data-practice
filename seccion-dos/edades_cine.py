edad = int(input("Ingrese su edad: "))
pelicula = input("Genero de la pelicula (terror/comedia/animacion): ")

if edad >= 0 and edad <= 12:
    print("EL usuario es un niño.")
    if pelicula == "terror":
        print("No se puede ingresar a ver la pelicula de terror, es para mayores de 12 años.")
    else:
        print("Puede ingresar a ver la pelicula.")

elif edad >= 13 and edad <= 17:
    print("EL usuario es un adolecente. \nPuede ingresar a ver la pelicula")
elif edad >= 18 and edad <= 64:
    print("EL usuario es un adulto. \nPuede ingresar a ver la pelicula")
elif edad >= 65:
    print("EL usuario es un adulto mayor. \nPuede ingresar a ver la pelicula")
else:
    print("Edad no valida.")