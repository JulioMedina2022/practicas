import string
def contar_palabras(texto):
    ignorar = texto.lower()
    conteo= {}
    for palabra in ignorar.split(): conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

texto = 'Hola, mundo.'. translate(str.maketrans('','', string.punctuation))
conteo_palabra = contar_palabras(texto)
print(conteo_palabra)