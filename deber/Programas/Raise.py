def evaluarnota(nota):
    if nota<0:
        raise ValueError("Valor incorrecto")
    elif nota>= 16:
        print("excelente")
    elif nota>=11:
        print("Excelente")
    else:
        print("Desaprobado")

evaluarnota(55)
