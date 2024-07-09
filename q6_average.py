# Faça um programa que leia 5 números e informe a soma e a média dos números.

# Write a program that reads 5 numbers and reports the sum and average of the numbers.

while True:
    try:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        n3 = int(input("Enter the third number: "))
        n4 = int(input("Enter the fourth number: "))
        n5 = int(input("Enter the fifth number: "))
        list = [n1,n2,n3,n4,n5]
        average = (sum(list)/5)
        print(f'\nThe sum of the numbers in total is: {sum(list)}')
        print(f'The average is: {average}')
        break
    except ValueError:
        print("Invalid value. Please, try again.")
        continue

