
# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25

def func(choice,lista):
    for i in range(1,choice+1):
        l = int(input("Digite o numero: "))
        lista.append(l)
    return lista

def maior_num(lista):
    if len(lista) < 2:
        return 'A lista deve conter pelo menos dois elementos.'
    maior_numero = max(lista[0],lista[1])
    segundo_maior = min(lista[0],lista[1])

    for elemento in lista[2:]:
        if elemento > maior_numero:
            segundo_maior = maior_numero
            maior_numero = elemento
        elif elemento > segundo_maior:
            segundo_maior = elemento

    return f'Primeiro maior: {maior_numero}\nSegundo maior: {segundo_maior}\nSoma: {maior_numero+segundo_maior}'

#assert
def Teste_maior():
    teste = [5,97,6]
    testando = maior_num(teste)
    assert testando == 'Primeiro maior: 97\nSegundo maior: 6\nSoma: 103', f"Erro: testando = {testando}"

Teste_maior()

while True:
    try:
        choice = int(input("\nQuantos elementos voce deseja que a lista tenha? "))
        lista = []
        lista_um = func(choice,lista)
        maior = maior_num(lista)
        print(f'\nLista original: {lista_um}')
        print(maior_num(lista))
    except:
        print("Erro! Tente novamente.")
