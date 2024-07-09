# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

# Make a program that asks for a note, between zero and ten. 
# Show a message if the value is invalid and continue asking until the user enters a valid value.

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





