import random
score = random.randint(0, 10)
print("Bienvenido a mi trivia sobre HISTORIA DEL PERÚ")
print("Pondremos a prueba tus conocimientos")
print("Cada acierto vale 5 puntos y cada error -2")
print("Comenzarás con",score,"puntos")
name = input("\nIngresa tu nombre: ")
print("\nHola", name,",responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
print("1. ¿Qué año se independizó Perú?")
print("a) 1536")
print("b) 1969")
print("c) 1821")
print("d) 1452")
response_1 = input("\nTu respuesta:")
while response_1 not in ("a", "b", "c", "d"):
	response_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if response_1 == "c":
  score += 5
  print("¡Muy bien", name, "!\n")
else:
  score -= 2
  print("¡Incorrecto", name, "!\n")
print("2. ¿Qué año fue la batalla de Ayacucho?")
print("a) 1572")
print("b) 1824")
print("c) 1776")
print("d) 1789")
response_2 = input("\nTu respuesta:")
while response_2 not in ("a", "b", "c", "d"):
	response_2 = input("Debes responder a, b, c o d. Ingresa   nuevamente tu respuesta: ")
if response_2 == "a":
  score -= 2
  print("¡Incorrecto", name, "! En 1572 fue la Ejecución de Tupac Amaru\n")
elif response_2 == "c":
  score -= 2
  print("¡Incorrecto", name,"! En 1776 fue la Independencia de los Estados unidos\n")
elif response_2 == "d":
  score -= 2
  print("¡Incorrecto", name, "! En 1789 fue la Revolución Francesa")
else:
  score += 5
  print("¡Sigue así",name,"!\n")
print("3. ¿Qué año se descubrió Macchu Picchu?")
print("a) 1687")
print("b) 1905")
print("c) 1850")
print("d) 1911")
response_3 = input("\nTu respuesta:")
while response_3 not in ("a", "b", "c", "d"):
	response_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if response_3 == "d":
  score += 5
  print("¡Excelente", name, "!\n")
else:
  score -= 2
  print("¡Incorrecto", name, "!\n")

print("Muchas gracias por jugar mi trivia de historia, obtuviste", score,"puntos.")