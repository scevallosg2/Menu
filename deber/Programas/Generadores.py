'''
def generarmultiplos7(limite):
    numero=1
    listadenumeros=[]

    while numero<= limite:
        listadenumeros.append(numero*7)
        numero=numero+1
    return listadenumeros
print(generarmultiplos7(10))
'''

def generarmultiplos7(limite):
    numero=1

    while numero<= limite:
        yield numero*7
        numero=numero+1

obtienemultiplo7=generarmultiplos7(10)
'''
#print(generarmultiplos7(10))
 
for n in obtienemultiplo7:
    print(n)
'''

print(next(obtienemultiplo7))
print("Aca hay 200 lineas de codigo...")
print(next(obtienemultiplo7))
print("Aca hay 1000 lineas de codigo...")
print(next(obtienemultiplo7))
