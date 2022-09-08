# Diccionarios : Son estructuras de datos que nos permiten almacenar distintos
# valores .
# Es que los datos se almacenan asociados a una clave única , tenemos una relación
# clave : valor
# Los elementos almacenados están en desorden , el orden es indiferente a la forma
# de almacenamiento .
miDiccionario = { " España " : " Madrid " , " Perú " : " Lima " , " Alemania " : " Berlin " }
print (miDiccionario [' Perú '])
print(miDiccionario)

miDiccionario["venezuela"]="caracas"
print(miDiccionario)
miDiccionario[" España "]="Barcelona"
print(miDiccionario)
del miDiccionario[" España "]
print(miDiccionario)
dic2={"garcia":"oscar",25:True, "sueldo":150.80}
print(dic2[25])
llaves=("España" ,"Francia", "Inglaterra")
dicpaises={llaves[0]:"Madrid",llaves[1]:"Paris",llaves[2]:"Londres" }
print(dicpaises)
Datosper={"Apellidos":"Garcia","Años":{1:2010,2:2011,3:2012,4:2013,5:2014}}
print(Datosper)
print(Datosper["Años"])
print(Datosper.get('Apellido',("Sebastian")))
print(Datosper.keys())
print(Datosper.values())
valores=list(Datosper.values())
print(valores)

