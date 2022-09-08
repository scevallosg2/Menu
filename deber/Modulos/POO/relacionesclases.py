class pais():
    def __init__(self, nom, presi):
        self.nombre = nom
        self.presidente = presi

    def __str__(self):
        txt="Pais: {0} - Presidente: {1}"
        return txt.format(self.nombre, self.presidente)

class ciudad():
    def __init__(self, nom,habi,pai):
        self.nombres = nom
        self.habitantes = habi
        self.Pais = pai

    def __str__(self):
        txt="Ciudad: {0} - N°Habitantes: {1} ({2})"
        return txt.format(self.nombres, self.habitantes, self.Pais)

class urbanizacion():
    def __init__(self,nom,ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        txt= "urbanizacion: {0} ({1})"
        return txt.format(self.nombre, self.ciudad)


pais1=pais( "Ecuador", "Sebastian Cevallos")
print(pais1)

ciudad1=ciudad("Guayaquil", 100000,pais1)
print(ciudad1)

urba1=urbanizacion("Prosperina", "Guayaquil")
print(urba1)
