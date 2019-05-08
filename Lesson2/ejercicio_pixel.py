# Pasar a escala de grises el color codificado en los elementos de la lista 'pixel'

pixel = [0.6, 0.3, 0.4]

# La intensidad en la esclaa de grises es el promedio de la intensidad de cada canal.

inten = (pixel[0]+pixel[1]+pixel[2]) / len(pixel)

print(inten)

# otra solucion

p = 0
for numerito in pixel:
    p += numerito
p = p / len(pixel)

print(p)

# Otra Solucion

promedio = sum(pixel) / len(pixel)
print(promedio)

# Pasar a blanco o negro segun el valor de intensidad. Si la intensidad es mayor a 0.5 es blanco

print('El pixel es')
if promedio > 0.5:
    print(' blanco')
else:
    print(' Negro')
