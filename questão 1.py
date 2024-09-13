# Função que verifica se um número é ímpar
def eh_impar(num):
    return num % 2 != 0

# Função que comprova a proposição
def quadrado_impar_prova(num):
    quadrado = num ** 2
    if eh_impar(quadrado):
        print(f"O quadrado de {num} é ímpar, logo {num} é ímpar.")
    else:
        print(f"O quadrado de {num} é par, logo {num} não é ímpar.")

# Testando a função
numeros = [2, 3, 4, 5, 6, 7, 8, 9]

for num in numeros:
    quadrado_impar_prova(num)
