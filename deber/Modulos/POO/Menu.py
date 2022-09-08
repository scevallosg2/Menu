import os
os.system("cls")
class menu:
    def _init_(self):
        pass

    def menu(self, opciones):
        print("***********MENÚ ***********")
        print("Digite Un Numero Correspondiente A Las Opciones Porfavor")
        for opcion in opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}] : ".format(len(opciones)))
        return opc
