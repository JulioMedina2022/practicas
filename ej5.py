cantidad = 0
suma = 0
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    cantidad += 1
    suma += n

print(f"Cantidad: {cantidad}, Suma: {suma}")
