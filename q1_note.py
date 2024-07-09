# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

# Make a program that asks for a note, between zero and ten. 
# Show a message if the value is invalid and continue asking until the user enters a valid value.

while True:
    note = input("Enter your note: ")
    try:
        note = int(note)
        if note >= 0 and note <= 10:
            print("Ok.")
            break
        else:
            print("Invalid number.")
    except ValueError:
            print("Invalid value. Please,try again.")





