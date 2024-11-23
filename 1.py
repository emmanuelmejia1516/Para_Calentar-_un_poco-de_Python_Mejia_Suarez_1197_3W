# Programa 1: Definir la función max() que devuelve el mayor de dos números
def max(a, b):
    if a > b:
        return a
    else:
        return b

# Ejemplo de uso
num1 = 5
num2 = 10
print(f"El mayor número es: {max(num1, num2)}")
