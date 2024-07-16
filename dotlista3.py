
# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25

def func(choice,lista):
    for i in range(1,choice+1):
        l = int(input("Digite o numero: "))
        lista.append(l)
    return lista

def maior_num(lista):
    for elemento in lista:
        if elemento > lista:
            return

#assert

while True:
    try:
        choice = int(input("\nQuantos elementos voce deseja que a lista tenha? "))
        lista = []
        lista_um = func(choice,lista)
        semrep = rep(lista)
        maior = maior_num(lista)
        print(f'\nLista original: {lista_um}')
        print(maior)
    except:
        print("Erro! Tente novamente.")
