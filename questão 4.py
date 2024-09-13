# Função que verifica se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função que verifica se um número é ímpar
def eh_impar(numero):
    return numero % 2 != 0

# Função que soma um número par e um número ímpar
def soma_par_impar(par, impar):
    if eh_par(par) and eh_impar(impar):
        soma = par + impar
        print(f"{par} + {impar} = {soma}")
        if eh_impar(soma):
            print("A soma é ímpar!")
        else:
            print("A soma não é ímpar, algo está errado.")
    else:
        print("Os números fornecidos não são par e ímpar, respectivamente.")

# Exemplo de uso
numero_par = 4
numero_impar = 3
soma_par_impar(numero_par, numero_impar)
