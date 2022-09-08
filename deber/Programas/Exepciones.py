num1=20
num2=2
#print("la division de {0} entre {1} es:".format(num1,num2,num1/num2))
try:
    resultado=num1/num2

except ZeroDivisionError:
    print("no se puede dividir entre 0")

finally:
    print("Yo siempre aparezco")

print("aqui termina mi programa")






