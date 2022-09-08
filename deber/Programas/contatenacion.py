texto1="Hola"
texto2= " Mundo "
textoFinal= (texto1 + ""+texto2)
print ( textoFinal )

print("El saludo es: %s %s" % (texto1,texto2))

saludofinal= "Saludo: {0} {1}".format( texto1,texto2)
print(saludofinal)

saludofinal2="saludo: {x} {y}".format( x=texto1 , y=texto2)
print(saludofinal2)
