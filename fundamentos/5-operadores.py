num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operadores aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma: {sum}")
print(f"Subtração: {sub}")
print(f"Divisão: {div}")
print(f"Multiplicação: {mult}")
print(f"Resto da divisão: {mod}")
print(f"Exponenciação: {exp}")

# Operadores de comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"{num1} é maior que {num2}? {bigger}")
print(f"{num1} é menor que {num2}? {smaller}")
print(f"{num1} é igual a {num2}? {equal}")
print(f"{num1} é diferente de {num2}? {different}")
print(f"{num1} é maior ou igual a {num2}? {bigger_equal}")
print(f"{num1} é menor ou igual a {num2}? {smaller_equal}")

# Operadores atribuição
num1 += 5  # num1 = num1 + 5
num1 -= 3  # num1 = num1 - 3
num1 *= 2  # num1 = num1 * 2
num1 /= 4  # num1 = num1 / 4