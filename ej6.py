def leer_entero(mensaje):
        while True:
            try:
                return int(input(mensaje)) 
            except ValueError:
                print("Ese no es un número entero, intente otra vez")


edad = leer_entero("Número entero: ")