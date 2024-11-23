# Programa 10: Función procedimiento() que imprime un histograma de una lista de números
def procedimiento(lista):
    for num in lista:
        print('*' * num)

# Ejemplo de uso
lista = [4, 9, 7]
print("Histograma:")
procedimiento(lista)
