'''
-------Fundamentos de Programacion     -----
-------Bryan Bismarck Bautista Alonso  -----
-------Modulo 3                        -----


'''



calificacion = float(input("Calificacion: "))

if calificacion >= 11: 
    print("Calificacion no valida")

elif calificacion < 0: 
    print("Calificacion no valida")
else: 
    if calificacion >= 9:
        print("Excelente")
    elif calificacion >= 8:
        print("Buen trabajo")
    elif calificacion >= 6: 
        print("Aprobado")
    else:
            print("Reprobado")



 

