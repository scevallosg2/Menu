print("--Cursos--")
print("Matematicas - Biologia - Lenguaje - Ciencias")
curso= input("ingrese el curso deseado: ")
if curso in ("Matematicas" , "Biologia" , "Lenguaje" , "Ciencias"):
    print("Curso {0} Seleccionado.".format(curso))
else:
    print("no existe ese curso")
    