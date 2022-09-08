# factorial: es el productos de los numeros positivos
#factorial de 5: 1*2*3*4*5=120

numero=int(input("ingrese un numero"))
factorial=1
for n in range(1,(numero+1)):
    factorial=factorial*n

print("el factorial de {0} es: {1}".format(numero, factorial))
