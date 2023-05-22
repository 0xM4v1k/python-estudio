"""
Genera código repetitivo similar a while
"""
# Por cada x in el rango de 0 a 10
"""
number = int(input("ingresa un número: "))

if number > 5:
    for number in range(number, 15,2): # range(start,stop,step)
        # Se ejecuta
        print(number)
elif number < 5:
    for number in range(number, -2, -1):
        print(number)
else:
    print("XD")
print('el numero es: ' + str(number))
"""
languages = ["Python", "Go", "Javascript", "Java","Typescript", "PHP"]

frameworks = ["Django", "Flask", "Piramid", "FastApi"]

#for lenguaje in  languages:
#    print(lenguaje)

#for lenguaje in languages:
#    if lenguaje == "Python":
#        print("el lenguaje de programacion es: " + str(lenguaje))

# Cuandp hay for anidados se recorre el primer for
for lenguaje in languages:
    for framework in frameworks:
        print(lenguaje, framework)

saludo = "Hola uwu"

for letra in saludo:
    print(letra)
