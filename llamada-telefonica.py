# determinar caunto es el costo de una llamada telefonica

print("------------------------------------------------")
print("--------CUAL ES EL COSTO DE LA LLAMADA----------")
print("------------------------------------------------")

# INPUT


T= int(input("Digite el valor de t: "))

#Procesing

if T<=3 : 
    rta = " de 300"
    print("El valor de la llamada es" + str(rta))
else:
    
    if T>3 :
     r= 300 + 50 * (T - 3 )

    print("El valor de la llamada es " + str(r))

#OUTPUT

print("------------------------------------------------")
print("--------------FIN DE LA LLAMADA-----------------")
print("------------------------------------------------")