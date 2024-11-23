# Programa 2: Definir la función max_de_tres() que devuelve el mayor de tres números
def max_de_tres(a, b, c):
    return max(max(a, b), c)

# Ejemplo de uso
num1 = 5
num2 = 10
num3 = 3
print(f"El mayor número entre {num1}, {num2} y {num3} es: {max_de_tres(num1, num2, num3)}")
