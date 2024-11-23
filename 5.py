# Programa 5: Función sumatoria() y multip() que suman y multiplican los números de una lista
def sumatoria(lista):
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso
lista = [1, 2, 3, 4]
print(f"La suma de los elementos es: {sumatoria(lista)}")
print(f"La multiplicación de los elementos es: {multip(lista)}")
