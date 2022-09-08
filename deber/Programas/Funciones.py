#funciones:es un conjunto de instrucciones uq realizan un proceso
#su principal ventaja es que nos ayudan a evitar codigo repetido
def saludar():
    print("cevallos")
    print("Sebastian")
    print("sebas")
    return "hola"

print(saludar())

def evaluarsueldomin(sueldo):
    if sueldo>850:
        print("usted gana mas del minimo")
    else:
        print("Usted gana menos que el minimo")

evaluarsueldomin(1200)