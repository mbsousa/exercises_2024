

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





