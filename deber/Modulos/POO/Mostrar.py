from Menu import menu
from Modulos.modulos import modulos
from Modulos.Paquete1.Funciones_cadena import contarletras
from Modulos.Paquete1.funciones_numericas import Multiplicar, potenciar

import os

os.system("cls")
var = menu()
lis = ["1)Hola mundo","2)Variables","3)Conversiones","4)Numeros Operacionales","5)Contatenacion","6)Cadenas","7)Tuplas","8)Listas","9)Diccionarios","10)Ingreso de datos","11)IF_ELSE","12)Funciones","13)Operadores Logicos","14)Operador Temario","15)IF_IN","16)Range","17)FOR","18)Factorial","19)While","20)BREAK","21)Genereadores","22)Generadores2","23)Excepciones","24)Raise","25)Modulos","26)PruebaPaquete","27)Persona","28)Curso","29)Cuenta","30)Herencia","31)Herencia multiple","32)Polimorfismo","33)Relaciones Clases","34)Salir"]
opcion=""

while opcion != "34":
    os.system("cls")
    opcion = var.menu(lis)
    if opcion == "1":
        print("hola mundo")
        input("Presione una tecla para continuar")

    elif opcion== "2":
        os.system("cls")
        nombre = "sebastian"
        print(nombre)
        edad = 19
        print(edad)
        edad = "true"
        print(edad)
        sueldo = 600.00
        print(sueldo)
        input("Presione una tecla para continuar")


    elif opcion == "3":
        os.system("cls")

        numero1 = "35"
        numero2 = "18"
        print(numero1 + numero2)

        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)

        sueldo = 1200.43
        suel = int(sueldo)
        print(suel)

        valor = 4500.89
        va = float(valor)
        print(va * 3)

        edad = 100
        print(len(str(edad)))
        input("Presione una tecla para continuar")

    elif opcion == "4":
        os.system("cls")
        entero = 23
        decimal = 31.78
        complejo = 12 + 5j
        # booleano = True
        """
        print ( entero )
        print ( decimal )
        print ( complejo )
        print ( booleano )
        """

        num1 = 20
        num2 = 4
        print("suma:", (num1 + num2))
        print("resta:", (num1 - num2))
        print("multiplicacion:", (num1 * num2))
        print("divicion:", (num1 // num2))
        print("potencia:", (num1 ** num2))
        input("Presione una tecla para continuar")

    elif opcion == "5":
        os.system("cls")

        texto1 = "Hola"
        texto2 = " Mundo "
        textoFinal = (texto1 + "" + texto2)
        print(textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        saludofinal = "Saludo: {0} {1}".format(texto1, texto2)
        print(saludofinal)

        saludofinal2 = "saludo: {x} {y}".format(x=texto1, y=texto2)
        print(saludofinal2)

        input("Presione una tecla para continuar")



    elif opcion == "6":
        os.system("cls")

        texto = "Bienvenidos al canal de sebastian"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())  # Convierte una cadena a un formato de titulo
        print(texto.find("al"))  # Posición donde encuentra la cadena o porción .
        print(texto.count("e"))  # Cantidad de ocurrencias de una letra o porción .

        textofinal = texto.replace("e", "3")
        print(textofinal)

        valor = texto.isnumeric()  # Arroja true o false dependiendo si es un número .
        print(valor)

        cadenaseparada = texto.split(" ")
        print(cadenaseparada)
        input("Presione una tecla para continuar")


    elif opcion == "7":
        os.system("cls")
        tupla = (1, 2, 3)
        print(tupla)
        tupla2 = (7, " Oscar ", True, 450.1, 16 + 7j, 15, " Felicidad ", False)
        print(tupla2)
        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)
        print(tupla2[1])
        # tupla2 [ 1 ] " Uskokrum "
        print(tupla2[-1])  # Acceder al último elemento .
        print(tupla2[0:4])
        print(tupla2[-2])

        a, b, c = tupla
        print(a)
        print(b)
        print(c)
        tuplafinal = tupla + tupla3
        print(tuplafinal)
        print(tuplafinal.count(3))
        print(tuplafinal.index(3))
        input("Presione una tecla para continuar")



    elif opcion == "8":
        os.system("cls")
        lista1 = ["oscar", 25, 98.3, True, "Flavio", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])
        print(lista1)
        print(lista1[0: 3])
        print(lista1[:2])
        print(lista1[3:])
        lista1.append("sebastian")
        print(lista1)
        lista1.insert(4, "Peru")
        print(lista1)
        lista1.extend(["Alejandro", 110, False])
        print(lista1)
        print(lista1.index("Flavio"))
        lista1.remove(56.3)
        print(lista1)
        lista1.pop()
        print(lista1)
        lista2 = ["chiclayo", "Irma"]
        lista3 = lista1 + lista2
        print(lista3)
        print(lista2 * 4)
        print("sebastian" in lista1)
        input("Presione una tecla para continuar")


    elif opcion == "9":
        os.system("cls")
        miDiccionario = {" España ": " Madrid ", " Perú ": " Lima ", " Alemania ": " Berlin "}
        print(miDiccionario[' Perú '])
        print(miDiccionario)

        miDiccionario["venezuela"] = "caracas"
        print(miDiccionario)
        miDiccionario[" España "] = "Barcelona"
        print(miDiccionario)
        del miDiccionario[" España "]
        print(miDiccionario)
        dic2 = {"garcia": "oscar", 25: True, "sueldo": 150.80}
        print(dic2[25])
        llaves = ("España", "Francia", "Inglaterra")
        dicpaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
        print(dicpaises)
        Datosper = {"Apellidos": "Garcia", "Años": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(Datosper)
        print(Datosper["Años"])
        print(Datosper.get('Apellido', ("Sebastian")))
        print(Datosper.keys())
        print(Datosper.values())
        valores = list(Datosper.values())
        print(valores)
        input("Presione una tecla para continuar")

    elif opcion == "10":
        os.system("cls")
        Nombre = input("INGRESE SU NOMBRE:")
        Edad = int(input("INGRESE SU EDAD:"))
        sueldo = float(input("Ingrese su sueldo"))
        print("Bienvenido:" + Nombre)
        edadf = Edad + 20
        print("Su edad es:", Edad)
        print("Su dentro de 20 años sera de:", edadf)
        print("Tu sueldo es", sueldo)
        input("Presione una tecla para continuar")

    elif opcion == "11":
        os.system("cls")
        Edad = int(input("Ingrese su edad"))

        if Edad > 18:
            print("Eres mayor de edad.")
        elif Edad == 18:
            print("usted tiene 18 años!")
        else:
            print("usted es menor de edad")
        input("Presione una tecla para continuar")


    elif opcion == "12":
        os.system("cls")
        def saludar():
            print("cevallos")
            print("Sebastian")
            print("sebas")
            return "hola"
        print(saludar())
        def evaluarsueldomin(sueldo):
            if sueldo > 850:
                print("usted gana mas del minimo")
            else:
                print("Usted gana menos que el minimo")
        evaluarsueldomin(1200)
        input("Presione una tecla para continuar")

    elif opcion == "13":
        os.system("cls")
        distancia = 400
        numerohermanos = 3
        salariopadres = 3000

        tienebeneficios = False
        if (distancia > 1000 and numerohermanos > 2) or salariopadres < 2000:
            tienebeneficios = True
        print(not tienebeneficios)

        if (5 > 3 and (8 > 6)):
            print("verdad")
        else:
            print("Es mentira")
        input("Presione una tecla para continuar")


    elif opcion == "14":
        os.system("cls")
        """
        string sexo;
        sexo=(10>20) ? "Hombre", "femenino";
        """
        sexos = ("Hombre", "mujer")
        posicion = True
        sexo = sexos[posicion]  # mujer
        print(sexo)
        sexo = sexos[not posicion]  # hombre
        print(sexo)
        input("Presione una tecla para continuar")

    elif opcion == "15":
        os.system("cls")
        print("Cursos")
        print("Matematicas - Biologia - Lenguaje - Ciencias")
        curso = input("ingrese el curso deseado: ")
        if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
            print("Curso {0} Seleccionado.".format(curso))
        else:
            print("no existe ese curso")
        input("Presione una tecla para continuar")


    elif opcion == "16":
        os.system("cls")
        numeros = range(5)  # [1,2,3,4,5]
        print(numeros[3])
        numeros1 = range(4, 10)  # [4,5,6,7,8,9,10]
        print(numeros1[2])
        numero2 = range(10, 100, 8)  # [10,18,26,34,42,50,58,66,74,82,90....]
        print(numero2[9])
        input("Presione una tecla para continuar")

    elif opcion == "17":
        os.system("cls")
        for i in range(1, 13):
            print("{0}x{1} es:{2}".format(i, i, (i * i)))
        for nom in ["Karen", "jose", "miguel", "leo"]:
            print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
        input("Presione una tecla para continuar")

    elif opcion == "18":
        numero = int(input("ingrese un numero: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n

        print("el factorial de {0} es: {1}".format(numero, factorial))
        input("Presione una tecla para continuar")


    elif opcion == "19":
        os.system("cls")
        """
        indice=1

        while indice<10:
            print("valor actual: {0}".format(indice))
            indice= indice+1

        print("terminado el bucle while")
        #continua
        """
        inicio = 2
        while inicio <= 100:
            print("numero par: {0}".format(inicio))
            inicio += 2
        print("terminado el bucle while")
        input("Presione una tecla para continuar")




    elif opcion == "20":
        os.system("cls")
        '''
        for numero in range (1,6):
            if  numero==3:
                break #decanso o interumpir
            print("El numero es: {0}".format(numero))

        print("Bucle terminado.")
        '''

        '''
        #omite una parte del bucle
        #continua con el resto

        for numero in range (1,6):
            if  numero==3:
                continue
            print("El numero es: {0}".format(numero))

        print("Bucle terminado.")
        '''

        # pass permite continuar con una sentencia o funcion que aun
        # no tiene un bloqque con codigo

        for numero in range(1, 6):
            if numero <= 3:
                pass
            else:
                print("el siguiente valor es mayor a 3")
            print("El numero es: {0}".format(numero))

        print("Bucle terminado.")
        input("Presione una tecla para continuar")



    elif opcion == "21":
        os.system("cls")
        '''
        def generarmultiplos7(limite):
            numero=1
            listadenumeros=[]

            while numero<= limite:
                listadenumeros.append(numero*7)
                numero=numero+1
            return listadenumeros
        print(generarmultiplos7(10))
        '''


        def generarmultiplos7(limite):
            numero = 1

            while numero <= limite:
                yield numero * 7
                numero = numero + 1


        obtienemultiplo7 = generarmultiplos7(10)
        '''
        #print(generarmultiplos7(10))

        for n in obtienemultiplo7:
            print(n)
        '''

        print(next(obtienemultiplo7))
        print("Aca hay 200 lineas de codigo...")
        print(next(obtienemultiplo7))
        print("Aca hay 1000 lineas de codigo...")
        print(next(obtienemultiplo7))
        input("Presione una tecla para continuar")




    elif opcion == "22":
        os.system("cls")
        def generarmultiplos7(limite):
            numero = 1

            while numero <= limite:
                yield numero * 7
                numero = numero + 1

        obtienemultiplo7 = generarmultiplos7(10)
        print(next(obtienemultiplo7))
        print("Aca hay 200 lineas de codigo...")
        print(next(obtienemultiplo7))
        print("Aca hay 1000 lineas de codigo...")
        print(next(obtienemultiplo7))
        input("Presione una tecla para continuar")



    elif opcion == "23":
        os.system("cls")
        num1 = 20
        num2 = 2
        # print("la division de {0} entre {1} es:".format(num1,num2,num1/num2))
        try:
            resultado = num1 / num2

        except ZeroDivisionError:
            print("no se puede dividir entre 0")

        finally:
            print("Yo siempre aparezco")

        print("aqui termina mi programa")
        input("Presione una tecla para continuar")



    elif opcion == "24":
        os.system("cls")
        def evaluarnota (nota):
            if nota < 0:
                raise ValueError("Valor incorrecto")
            elif nota >= 16:
                print("excelente")
            elif nota >= 11:
                print("Excelente")
            else:
                print("Desaprobado")
        evaluarnota(55)

        input("Presione una tecla para continuar")

    elif opcion == "25":
        os.system("cls")
        modulos()
        input("Presione una tecla para continuar")

    elif opcion == "26":
        os.system("cls")
        print(Multiplicar(5,6))
        print(potenciar(5,6))
        print(contarletras("Sebastian"))

        input("Presione una tecla para continuar")


    elif opcion == "27":
        os.system("cls")

        class Persona():
            # prpiedades
            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False

            # Funcionalidades
            def despertar(self):
                self.despierta = True
                print("Buenos Dias")


        persona1 = Persona()
        persona1.apellidos = "Cevallos Garcia"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellidos = "Garcia Cevallos"
        print(persona2.apellidos)
        # persona2.despertar()
        print(persona2.despierta)
        input("Presione una tecla para continuar")


    elif opcion == "28":
        os.system("cls")


        class curso():
            """"
            nombre= "matematicas"
            creditos="5"
            profesion="Ingenieria software"
        """""

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "presencial"

            def Mostrardatos(self):
                dat = "nombre: {0} / creditos:{1} / imparticion:{2}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteasignado = self.__verificardocente()
                if docenteasignado:
                    print("Existe docente asignado")
                else:
                    print("No es necesario asignar docente")

            def __verificardocente(self):
                print("verificando si existe docente asignado")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "nombre: {0} - creditos:{1}"
                return texto.format(self.nombre, self.creditos)


        curso1 = curso("matematicas", 5, "Ingenieria software")
        print(curso1)

        curso1.Mostrardatos()
        """
        curso2=curso("lengua",4,"Ingenieria civil")
        print(curso2.nombre)
        """
        input("Presione una tecla para continuar")


    elif opcion == "29":
        os.system("cls")

        class cuenta():

            def __init__(self, pro, sal, mode):
                self.__propietario = pro
                self.__Saldo = sal
                self.__moneda = mode

            # Getters (metodos Get)

            def get_Saldo(self):
                return self.__Saldo

            def get_Propietario(self):
                return self.__propietario

            def get_Moneda(self):
                return self.__moneda

            # setter (metodos Set)
            def set_moneda(self, moneda):
                self.__moneda = moneda


        cuenta1 = cuenta("Sebastian Cevallos", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_moneda("Dolares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar")


    elif opcion == "30":
        os.system("cls")


        class persona():

            def __init__(self, apepa, apema, nom):
                self.apellidopaterno = apepa
                self.apellidomaterno = apema
                self.nombrec = nom

            def mostrarnombrecompleto(self):
                txt = "{0},{1},{2}"
                return txt.format(self.apellidopaterno, self.apellidomaterno, self.nombrec)

            def datos(self):
                print(self.mostrarnombrecompleto())


        class estudiante(persona):
            def __init__(self, apepa, apema, nom, pro):
                super().__init__(apepa, apema, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesion: {0}".format(self.profesion))


        # estu1=estudiante("Cevallos","Garcia","Sebastian","ING En Software")
        estu1 = persona("Cevallos", "Garcia", "Sebastian")

        # print(estu1.mostrarnombrecompleto())
        # print(estu1.profesion)
        # estu1.datos()
        print(isinstance(estu1, persona))
        input("Presione una tecla para continuar")

    elif opcion == "31":
        os.system("cls")


        class claseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2


        class claseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class clasex(claseA, claseB):
            pass

        cx1 = clasex(15, 21)
        input("Presione una tecla para continuar")



    elif opcion == "32":
        os.system("cls")


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

        doc1 = trabajador()
        describirpersona(doc1)

        input("Presione una tecla para continuar")



    elif opcion == "33":
        os.system("cls")

        class pais():
            def __init__(self, nom, presi):
                self.nombre = nom
                self.presidente = presi

            def __str__(self):
                txt = "Pais: {0} - Presidente: {1}"
                return txt.format(self.nombre, self.presidente)


        class ciudad():
            def __init__(self, nom, habi, pai):
                self.nombres = nom
                self.habitantes = habi
                self.Pais = pai

            def __str__(self):
                txt = "Ciudad: {0} - N°Habitantes: {1} ({2})"
                return txt.format(self.nombres, self.habitantes, self.Pais)


        class urbanizacion():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "urbanizacion: {0} ({1})"
                return txt.format(self.nombre, self.ciudad)


        pais1 = pais("Ecuador", "Sebastian Cevallos")
        print(pais1)

        ciudad1 = ciudad("Guayaquil", 100000, pais1)
        print(ciudad1)

        urba1 = urbanizacion("Prosperina", "Guayaquil")
        print(urba1)
        input("Presione una tecla para continuar")


    elif opcion == "34":
        os.system("cls")
        print("Gracias por usar nuestro Menu")