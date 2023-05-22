#condicion = (if) True => ejecuta código
#condicion = False => ejecuta otra porción de código

edad_persona = int(input("Ingresa tu edad: "))

Edad = 18

if edad_persona >= Edad:
    print("Ya puedes ir a las cariñosas")
    if edad_persona >=60:
        print("Ya toca tomar tu viagra")
elif edad_persona == 17:
    print("Primero tramita tu DNI") 
else:
    print("Anda toma tu biberón")


