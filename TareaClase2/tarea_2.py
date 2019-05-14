#  Calcular el promedio de una lista de numeros

values = [5, 6, 10, 13, 3, 4]
sum_values = sum(values)
len_values = len(values)
prom = sum_values/len_values

print "El promedio de todos los numeros de la lista es: %.2f" % prom

# Calcular las alturas de diferentes gruoos de personas y determinar cual grupo posee la altura maxima.

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

# calcular el maximo valor en cada sublista
each_max = [max(p) for p in todos]

#print each_max

cont = 0
for i in each_max:
    if i > cont:
        cont = i
print "El maximo valor es: ", cont,"Y se encuentra en el grupo:" , (each_max.index(cont)+1)
