
# Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

def func(choice,lista):
    for i in range(1,choice+1):
        l = int(input("Digite o numero: "))
        lista.append(l)
    return lista

def conta(lista):
    resultado = ""
    for elemento in set(lista):
        cont = lista.count(elemento)
        resultado += f'O elemento {elemento} se repete {cont} vezes.\n'
    return resultado

#assert
def Teste_conta():
    teste = [8, 9, 9]
    testando = conta(teste)
    assert testando == 'O elemento 8 se repete 1 vezes.\nO elemento 9 se repete 2 vezes.\n', f"Erro: testando: {testando}"
Teste_conta()

while True:
    try:
        choice = int(input("\nQuantos elementos voce deseja que a lista tenha? "))
        lista = []
        lista_um = func(choice,lista)
        cont = conta(lista)
        print(f'\nLista original: {lista_um}')
        print(cont)
    except:
        print("Erro! Tente novamente.")
