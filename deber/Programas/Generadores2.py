def devuelvelenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng


lenguajesobtenidos= devuelvelenguajes("python","Java","PHP","Ruby","JavaScript")
print(next(lenguajesobtenidos))
print(next(lenguajesobtenidos))
