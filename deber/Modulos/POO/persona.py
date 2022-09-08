class Persona():
    #prpiedades
    apellidos=""
    nombres=""
    edad=0
    despierta = False

    #Funcionalidades
    def despertar(self):
        self.despierta=True
        print("Buenos Dias")

persona1 = Persona()
persona1.apellidos= "Cevallos Garcia"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)


persona2 = Persona()
persona2.apellidos= "Garcia Cevallos"
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)