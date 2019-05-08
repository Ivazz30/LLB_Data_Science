tupla = (1, 'a', True)

print(tupla)

# Agregar mas elementos

tupla = tupla + (8, 'c')
print(tupla)

# simplificado
tupla += (9, 878)
print(tupla)

# sub tupla
# imprimir el penultimo

print(tupla[1:-1])

# subtupla con saltos posiciones pares

print(tupla[::2])

# subtupla con saltos posiciones imppares
print(tupla[1::2])

