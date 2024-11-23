# Programa 8: Función superposicion() que verifica si dos listas tienen al menos un miembro en común
def superposicion(lista1, lista2):
    for a in lista1:
        for b in lista2:
            if a == b:
                return True
    return False

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
print(f"¿Las listas tienen elementos en común? {superposicion(lista1, lista2)}")

lista3 = [6, 7, 8]
print(f"¿Las listas tienen elementos en común? {superposicion(lista1, lista3)}")

