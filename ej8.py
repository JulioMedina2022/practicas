notas = [4.0, 2.5, 5.0, 3.0, 1.8]

prom = sum(notas)/len(notas)  # promedio
maximo = max(notas) # nota máxima en la lista
debajo_prom = [n for n in notas if n < prom] # Números debajo del promedio

print(f'El promedio es de:{prom:.2f}')
print(f'La nota máxima es de:{maximo}')
print(f'Debajo del promedio:{len(debajo_prom)}')