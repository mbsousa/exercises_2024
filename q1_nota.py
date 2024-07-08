# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

while True:
    nota = input("Digite sua nota: ")
    try:
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            print("Ok.")
            break
        else:
            print("Numero invalido")
    except ValueError:
            print("Valor invalido.Tente novamente.")





