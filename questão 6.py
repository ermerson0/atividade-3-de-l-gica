def divide(x, y):
    return y % x == 0

def prova_divisibilidade(a, b, c):
    if divide(a, b) and divide(b, c):
        print(f"{a} divide {b} e {b} divide {c}, portanto {a} também divide {c}.")
    else:
        print(f"A condição não é satisfeita para {a}, {b}, {c}.")

# Exemplo de uso
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

prova_divisibilidade(a, b, c)
