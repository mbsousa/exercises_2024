
# Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

def func(choice,lista):
    for i in range(1,choice+1):
        l = int(input("Digite o numero: "))
        lista.append(l)
    return lista

def rep(lista):
    sem_repetir = []
    for elemento in lista:
        if elemento not in sem_repetir:
            sem_repetir.append(elemento)
    return sem_repetir

#assert
def testar_rep():
    teste = [1,2,3,3,4,5,3,6,7]
    sem_repetir = rep(teste)
    assert  sem_repetir == [1,2,3,4,5,6,7], f"Erro: sem_repetir = {sem_repetir}"

testar_rep()

while True:
    try:
        choice = int(input("\nQuantos elementos voce deseja que a lista tenha? "))
        lista = []
        lista_um = func(choice,lista)
        semrep = rep(lista)
        print(f'\nLista original: {lista_um}')
        print(f'\nLista sem repetições: {semrep}')
    except:
        print("Erro! Tente novamente.")
