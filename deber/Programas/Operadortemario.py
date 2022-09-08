"""
string sexo;
sexo=(10>20) ? "Hombre", "femenino";
"""
sexos=("Hombre", "mujer")
posicion= True
sexo = sexos[posicion] #mujer
print(sexo)
sexo = sexos[not posicion] #hombre
print(sexo)
