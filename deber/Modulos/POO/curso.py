class curso():
    """"
    nombre= "matematicas"
    creditos="5"
    profesion="Ingenieria software"
"""""
    def __init__(self ,nom, cre,pro):
        self.nombre=nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion= "presencial"


    def Mostrardatos(self):
        dat= "nombre: {0} / creditos:{1} / imparticion:{2}"
        print(dat.format( self.nombre, self.creditos, self.__imparticion))
        docenteasignado=self.__verificardocente()
        if docenteasignado:
            print("Existe docente asignado")
        else:
            print("No es necesario asignar docente")



    def __verificardocente(self):
        print("verificando si existe docente asignado")
        if self.__imparticion=="Presencial":
            return True
        else:
            return False

    def __str__(self):
        texto="nombre: {0} - creditos:{1}"
        return texto.format(self.nombre, self.creditos)


curso1=curso("matematicas",5,"Ingenieria software")
print(curso1)

curso1.Mostrardatos()
"""
curso2=curso("lengua",4,"Ingenieria civil")
print(curso2.nombre)
"""