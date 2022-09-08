class cuenta():

    def __init__(self, pro, sal, mode):
        self .__propietario= pro
        self .__Saldo=sal
        self .__moneda=mode

    #Getters (metodos Get)

    def get_Saldo(self):
        return self.__Saldo

    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda

    # setter (metodos Set)
    def set_moneda(self,moneda):
        self.__moneda=moneda


cuenta1= cuenta("Sebastian Cevallos", 15000,"Soles")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_moneda("Dolares")
print(cuenta1.get_Moneda())


