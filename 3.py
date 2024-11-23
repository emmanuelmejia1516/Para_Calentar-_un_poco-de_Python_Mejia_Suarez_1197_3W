# Programa 3: Función que calcula la longitud de una lista o cadena
def longitud(obj):
    contador = 0
    for i in obj:
        contador += 1
    return contador

# Ejemplo de uso
cadena = "Hola mundo"
lista = [1, 2, 3, 4, 5]
print(f"La longitud de la cadena es: {longitud(cadena)}")
print(f"La longitud de la lista es: {longitud(lista)}")
