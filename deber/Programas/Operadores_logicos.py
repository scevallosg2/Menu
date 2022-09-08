#AND=y si ademas
#OR= o sino
#NOT= negacion

distancia=400
numerohermanos=3
salariopadres=3000

tienebeneficios=False
if(distancia>1000 and numerohermanos>2) or salariopadres<2000:
    tienebeneficios=True

print(not tienebeneficios)

if(5>3 and (8>6)):
    print("verdad" )
else:
    print("Es mentira")
