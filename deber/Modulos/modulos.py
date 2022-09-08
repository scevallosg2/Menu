'''
modulo
es un archuivo con extension .py o pyc (python compilado),
que posee su propioespacios de nombre y se puede contener variables,
funciones, clases o incluso otros modulos.

¿Para que sirven?
para organizar mejor el codigo y poder reutizar nuestro codigo mejor
Modularizacion y la reutilizacion.
'''

#import FuncionesMate

from Modulos.FuncionesMate import sumar , multi
def modulos():
    print(sumar(5,6))
    print(multi(5,6))

