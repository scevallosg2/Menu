texto="Bienvenidos al canal de sebastian"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title()) #Convierte una cadena a un formato de titulo
print(texto.find("al")) # Posición donde encuentra la cadena o porción .
print(texto.count("e")) # Cantidad de ocurrencias de una letra o porción .

textofinal= texto.replace("e","3")
print(textofinal)

valor = texto.isnumeric ( ) # Arroja true o false dependiendo si es un número .
print ( valor )

cadenaseparada= texto.split(" ")
print(cadenaseparada)
