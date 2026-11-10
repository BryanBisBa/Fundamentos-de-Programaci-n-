'''
Programa para estudiar los elementos de el lenguaje de programacion de Python 
Mi nombre es Bryan Bismarck Bautista 
'''

nombre = "Ana" #Variable tipo String 
edad = 19 # Variable tipo let 
estatura = 1.65 # Variable tipo float 
es_estudiante = True #Variable tipo boolen 

# Imprimimos la variable y su tipo 
print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Estudiante:", es_estudiante, type(es_estudiante))

# Declaro una constante 
PROMEDIO_MINIMO = 6

# Introducimos datos y los guardamos en las variables materia y calificacion 
materia = input("¿Que materia cursas? ")
calificacion = float(input("¿Que calificacion tienes? "))

# Hacemos operaciones basicas 
suma = 8+2 
resto = 10 % 3 
potencia = 2 ** 3 

# Estamos declarando dos variables de tipo booleanas 
mayor_de_edad = edad >= 18 
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante


# Imprimimos el resultado
print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia) 
print("¿Mayor de edad?", mayor_de_edad) 