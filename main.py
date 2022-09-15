import random
puntaje = random.randint(0, 10)
print("Bienvenido a mi trivia sobre HISTORIA DEL PERÚ")
print("Pondremos a prueba tus conocimientos")
print("Cada acierto vale 5 puntos y cada error -2")
print("Comenzarás con",puntaje,"puntos")
nombre = input("\nIngresa tu nombre: ")
print("\nHola", nombre,",responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
print("1. ¿Qué año se independizó Perú?")
print("a) 1536")
print("b) 1969")
print("c) 1821")
print("d) 1452")
respuesta_1 = input("\nTu respuesta:")
while respuesta_1 not in ("a", "b", "c", "d"):
	respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "c":
  puntaje += 5
  print("¡Muy bien", nombre, "!\n")
else:
  puntaje -= 2
  print("¡Incorrecto", nombre, "!\n")
print("2. ¿Qué año fue la batalla de Ayacucho?")
print("a) 1572")
print("b) 1824")
print("c) 1776")
print("d) 1789")
respuesta_2 = input("\nTu respuesta:")
while respuesta_2 not in ("a", "b", "c", "d"):
	respuesta_2 = input("Debes responder a, b, c o d. Ingresa   nuevamente tu respuesta: ")
if respuesta_2 == "a":
  puntaje -= 2
  print("¡Incorrecto", nombre, "! En 1572 fue la Ejecución de Tupac Amaru\n")
elif respuesta_2 == "c":
  puntaje -= 2
  print("¡Incorrecto", nombre,"! En 1776 fue la Independencia de los Estados unidos\n")
elif respuesta_2 == "d":
  puntaje -= 2
  print("¡Incorrecto", nombre, "! En 1789 fue la Revolución Francesa")
else:
  puntaje += 5
  print("¡Sigue así",nombre,"!\n")
print("3. ¿Qué año se descubrió Macchu Picchu?")
print("a) 1687")
print("b) 1905")
print("c) 1850")
print("d) 1911")
respuesta_3 = input("\nTu respuesta:")
while respuesta_3 not in ("a", "b", "c", "d"):
	respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_3 == "d":
  puntaje += 5
  print("¡Excelente", nombre, "!\n")
else:
  puntaje -= 2
  print("¡Incorrecto", nombre, "!\n")

print("Muchas gracias por jugar mi trivia de historia, obtuviste", puntaje,"puntos.")