class persona():

    def __init__(self, apepa,apema,nom):
        self.apellidopaterno=apepa
        self.apellidomaterno = apema
        self.nombrec = nom
    def mostrarnombrecompleto(self):
        txt="{0},{1},{2}"
        return txt.format(self.apellidopaterno,self.apellidomaterno,self.nombrec)

    def datos(self):
        print(self.mostrarnombrecompleto())


class estudiante(persona):
    def __init__(self,apepa,apema,nom,pro):
        super().__init__(apepa,apema,nom)
        self.profesion=pro

    def datos(self):
        super().datos()
        print("Profesion: {0}".format(self.profesion))

#estu1=estudiante("Cevallos","Garcia","Sebastian","ING En Software")
estu1=persona("Cevallos","Garcia","Sebastian")

#print(estu1.mostrarnombrecompleto())
#print(estu1.profesion)
#estu1.datos()
print(isinstance(estu1,persona))

