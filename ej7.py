def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje)) # retorna el numero si es entero.
        except ValueError:
            print("Ese no es un número entero, intente otra vez") # sigue el bucle hasta que se escriba un número entero.

def sumar(lista):
        suma = 0
        for i in lista: suma += i # Suma cada número de la lista.
        return suma

def contar(lista):
        cantidad =0
        for c in lista: cantidad +=1 # Cuenta cuantos números en total tiene la lista.
        return cantidad

lista = []
while True:
    n= leer_entero("Número entero: ")
    if n == 0:
        break
    lista.append(n)

print(f"La cantidad total es de: {contar(lista)} y la suma total es de: {sumar(lista)}")
