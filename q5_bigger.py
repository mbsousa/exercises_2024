# Faça um programa que leia 5 números e informe o maior número.

# Write a program that reads 5 numbers and reports the largest number.

while True:
    try: 
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        n3 = int(input("Enter the third number: "))
        n4 = int(input("Enter the fourth number: "))
        n5 = int(input("Enter the fifth number: "))
        if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
            print(f"The biggest one is the first number")
            break
        elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
            print(f"The biggest one is the second number")
            break
        elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
            print(f"The biggest one is the third number")
            break
        elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
            print(f"The biggest one is the fourth number.")
            break
        elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
            print(f"The biggest one is the fifth number.")
            break
    except ValueError:
        print("Invalid value. Please, try again.")
        print("\n")
        continue
