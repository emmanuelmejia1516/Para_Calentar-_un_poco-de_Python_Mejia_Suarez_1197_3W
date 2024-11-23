# Programa 7: Función es_palindromo() que reconoce palíndromos
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Ejemplo de uso
palabra = "radar"
print(f"La palabra '{palabra}' es un palíndromo: {es_palindromo(palabra)}")

palabra = "python"
print(f"La palabra '{palabra}' es un palíndromo: {es_palindromo(palabra)}")
