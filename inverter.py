# Define a função 'receber_numero' que solicita ao usuário um número inteiro,
# repetindo até que seja fornecido um valor válido. Retorna o número.

def receber_numero():
    while True:
        try:
            num = int(input("Digite um número para verificação: "))
            return num
        except ValueError:
            print("Favor digite um numero inteiro valido")

# Define a função 'criar_listas_numeros' que cria uma lista de 10 números
# inteiros fornecidos pelo usuário usando a função 'receber_numero'. Retorna a lista.

def criar_listas_numeros():
    lista = []
    for _ in range(10):
        numero = receber_numero()
        lista.append(numero)
    return lista

# Define a função 'cria_listas' que recebe um número inteiro como argumento e
# cria três listas: uma contendo todos os números de 0 até esse número, outra com
# os números pares até esse número, e a terceira com os números ímpares até esse número.
# Retorna as três listas.

def cria_listas(numero):
    numeros_inferiores = []
    par = []
    impar = []
    for aux in range(numero+1):
        numeros_inferiores.append(aux)
        if aux % 2 == 0:
            par.append(aux)
        else:
            impar.append(aux)
    return numeros_inferiores, par, impar

# Define a função 'imprimir' que recebe três listas como argumento e imprime cada uma delas.

def imprimir(numeros_inferiores, par, impar):
    print("Esta é a lista dos números inferiores:", numeros_inferiores)
    print("Esta é a lista dos números pares:", par)
    print("Esta é a lista dos números ímpares:", impar)

# Chama a função 'receber_numero' para obter um número do usuário.
numero = receber_numero()

# Chama a função 'cria_listas' com o número fornecido e armazena as três listas retornadas.
numeros_inferiores, par, impar = cria_listas(numero)

# Chama a função 'imprimir' para imprimir as três listas.
imprimir(numeros_inferiores, par, impar)

# Chama a função 'criar_listas_numeros' para criar uma lista de 10 números fornecidos pelo usuário.
lista = criar_listas_numeros()

# Cria uma lista total combinando as listas de números inferiores, pares, ímpares e a lista adicional.
lista_total = numeros_inferiores + par + impar + lista

# Inverte a ordem da lista total.
lista_total.reverse()

# Imprime a lista total invertida.
print("Lista total invertida", lista_total)

# Imprime a lista adicional fornecida pelo usuário.
print(lista)
