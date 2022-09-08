class estudiante():
     def describir(self):
         print("soy un buen estudiante")


class docente():
    def describir(self):
        print("Me dedico a enseñar cursos")


class trabajador():
    def describir(self):
        print("trabajo dentro de una gran empresa")

def describirpersona(persona):
    persona.describir()

doc1=trabajador()
describirpersona(doc1)

