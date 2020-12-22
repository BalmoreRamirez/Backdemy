import cmath
""" TIPOS DE VARIABLES"""

"""
str = String
int = Integer
float =  Float
bool = Booleano
"""
nombre = 'Jonathan'
edad = 21
estatura = 1.70
estadoUsuario = True

print(type(estadoUsuario))


""" OPERADORES """

""" Aritméticos: """
suma = 2 + 1
resta = 2 - 1
division = 15 / 2
modulo = 15 % 2
floorDivision = 15 // 2
multiplicacion = 5 * 2
exponente = 5 ** 2

"""Variantes cortas:

Variante:            Es igual a:
x += 1                x = x + 1
x -= 1                x = x - 1
x *= 1                x = x * 1
x /= 1                x = x / 1
"""

respuestas = {"Suma": suma, "Resta": resta,
              "Divisón": division, "Módulo": modulo,
              "Floor": floorDivision, "Multiplicación": multiplicacion,
              "Exponente": exponente}
print(respuestas)

"""
Lógicos:

and, or, not

Relacionales:

==, !=, <, >, <=, >=

"""

"""BUCLES"""

"""While:"""

i = 1
while i > 6:
    print(i)
    i += 1
    


"""For:"""
coloresFrutas = ["rojo", "amarillo", "rosa"]
frutas = ["manzana", "banana", "cereza"]

for x in frutas:
  for y in coloresFrutas:
      print(x,y)


"""FUNCIONES"""

def AreaCuadrado(lado):
    area = lado ** 2
    return area, lado

areaCuadrado = AreaCuadrado(2)
print("El área del cuadrado de "+ str(areaCuadrado[1]) + " es: "+ str(areaCuadrado[0]))

"""FLUJOS DE CONTROL:"""

if areaCuadrado[0] > 6:
    while areaCuadrado[0] > 6:
        areaCuadrado[0] -= 0.1

    print("El área se redujo a: ")
    print(areaCuadrado[0])

else:
    print("No se ha reducido el área")

lucesDeNavidad = {"Estado": True,
                  "Color": "amarillas",
                  "Tamaño": 3,
                  "Switch": None
                  }

if (lucesDeNavidad['Estado'] != False):
    if(lucesDeNavidad['Tamaño'] >= 2):
        if(lucesDeNavidad['Color'] == 'amarillas'):
            print('Adquiridas')
            lucesDeNavidad['Switch'] = 1
            if(lucesDeNavidad['Switch'] == 1):
                print('luces instaladas')
                print('Especificaciones: ')
                print(lucesDeNavidad)
        if(lucesDeNavidad['Color'] != 'amarillas'):
            print('Las luces no son amarillas, son de color '+ lucesDeNavidad['Color'])
    if(lucesDeNavidad['Tamaño'] < 2):
        print('Las luces no son de 2m, su largo es de '+str(lucesDeNavidad['Tamaño'])+'m')
else:
    print('Estas luces de Navidad no sirven')
