# Verifica se o produto de dois números ímpares é ímpar
num1 = int(input("Digite o primeiro número ímpar: "))
num2 = int(input("Digite o segundo número ímpar: "))

produto = num1 * num2

if produto % 2 != 0:
    print(f"O produto de {num1} e {num2} é {produto}, que é ímpar.")
else:
    print(f"O produto de {num1} e {num2} é {produto}, que não é ímpar.")
