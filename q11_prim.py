
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# Write a program that asks for an integer and determines whether or not it is a prime number.
# A prime number is one that is divisible only by itself and 1.


while True:
    try:
        num = int(input("Enter a number: "))
        cont = 0
        for i in range(1,num+1):
            if num % i == 0:
                cont += 1
        if cont == 2:
            print('The number entered is a prime.')
            break
        else:
            print('The number entered is not a prime.')
    except ValueError:
        print("Invalid number.")
