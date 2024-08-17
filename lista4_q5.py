# Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
# [1,3,6]

def func(choice,lista):
    for i in range(1,choice+1):
        l = int(input("Digite um número: "))
        lista.append(l)
    return lista

def lista_cumulativa(lista):
    if len(lista) < 2:
        return "A lista deve conter pelo menos dois elementos."

    list = [lista[0]]
    contador = lista[0]
    for i in lista[1:]:
        contador += i
        list.append(contador)
    return f'Lista cumulativa: {list}'

#assert
def testar_lista():
    teste = [1,2,3]
    testando = lista_cumulativa(teste)
    assert testando == 'Lista original: [1,2,3]\nLista cumulativa: [1,3,6]', f'Erro: testando={testando}'

while True:
    try:
        choice = int(input("\nQuantos elementos você deseja que a lista tenha? "))
        lista = []
        lista_um = func(choice,lista)
        lista_dois = lista_cumulativa(lista)
        print(f'\nLista original: {lista_um}')
        print(f'{lista_dois}')
    except:
        print('Erro! Tente novamente.')