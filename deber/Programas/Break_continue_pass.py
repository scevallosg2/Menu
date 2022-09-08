#break permite salir de un bucle cuando no cumple condicion
'''
for numero in range (1,6):
    if  numero==3:
        break #decanso o interumpir
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
'''


'''
#omite una parte del bucle
#continua con el resto

for numero in range (1,6):
    if  numero==3:
        continue
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
'''


#pass permite continuar con una sentencia o funcion que aun
#no tiene un bloqque con codigo

for numero in range (1,6):
    if  numero<=3:
        pass
    else:
        print("el siguiente valor es mayor a 3")
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")




