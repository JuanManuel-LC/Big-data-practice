# PROYECTO: Quiz de cultura general

preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["Londres", "Berlín", "París", "Roma"],
        "correcta": 3
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Saturno", "Júpiter", "Neptuno"],
        "correcta": 2  # posición contando desde 1 (Júpiter es la 2ª opción)
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "opciones": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"],
        "correcta": 3
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Nilo", "Amazonas", "Yangtsé"],
        "correcta": 2
    },
    {
        "pregunta": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
        "opciones": ["1776", "1789", "1804"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado en el mundo?",
        "opciones": ["Inglés", "Chino mandarín", "Español"],
        "correcta": 2
    }
    
]

def hacer_pregunta(pregunta_dict, numero):
    """Hacer la pregunta y devolver True si la respuesta es correcta, False si es incorrecta."""
    print()
    print(f"Pregunta {numero}: {pregunta_dict['pregunta']}")
    for i in range(len(pregunta_dict['opciones'])):
        print(f"{i + 1} {pregunta_dict['opciones'][i]}") 
    
    respuesta = int(input("Respuesta: "))
    
    if respuesta == pregunta_dict['correcta']:
        print(" ✅ ¡Correcto!")
        return True
    else:
        correcta = pregunta_dict['opciones'][pregunta_dict['correcta'] - 1]
        print(f"  ❌ Incorrecto. La respuesta era: {correcta}")
        return False

def mostrar_resultado(aciertos, total):
    """Sacamos el porcentaje de los aciertos e imprimimos el resultado"""
    porcentaje = (aciertos / total) * 100
    print("")
    print(f" === Resultado final. === ")
    print(f" Aciertos: {aciertos}/{total} ({porcentaje:.0f}%)")
    
    if porcentaje == 100:
        print("  🏆 ¡Perfecto! Eres un genio.")
    elif porcentaje >= 60:
        print("  👍 ¡Bien hecho! Aprobado.")
    else:
        print("  📚 Sigue estudiando. ¡Tú puedes!")
        

# Programa principal

print("  === QUIZ DE CULTURA GENERAL ===")
aciertos = 0
for i in range(len(preguntas)):
    if hacer_pregunta(preguntas[i], i + 1):
        aciertos = aciertos + 1
        
mostrar_resultado(aciertos, len(preguntas))