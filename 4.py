# Programa 4: Función que devuelve True si el carácter es una vocal, False de lo contrario
def es_vocal(caracter):
    if caracter.lower() in "aeiou":
        return True
    return False

# Ejemplo de uso
caracter = 'a'
print(f"El carácter '{caracter}' es vocal: {es_vocal(caracter)}")

caracter = 'b'
print(f"El carácter '{caracter}' es vocal: {es_vocal(caracter)}")
