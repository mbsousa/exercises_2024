# Faça um programa que leia 5 números e informe o maior número.

# Write a program that reads 5 numbers and reports the largest number.

while True:
    one = input("Enter the first number: ")
    two = input("Enter the second number: ")
    three = input("Enter the third number: ")
    four = input("Enter the fourth number: ")
    five = input("Enter the fifth number: ")
    try:
        one = int(one)
        two = int(two)
        three = int(three)
        four = int(four)
        five = int(five)
        if one > two and one > three and one > four and one > five:
            print(f"The biggest one is the first number")
            break
        elif two > one and two > three and two > four and two > five:
            print(f"The biggest one is the second number")
            break
        elif three > one and three > two and three > four and three > five:
            print(f"The biggest one is the third number")
            break
        elif four > one and four > two and four > three and four > five:
            print(f"The biggest one is the fourth number.")
            break
        elif five > one and five > two and five > three and five > four:
            print(f"The biggest one is the fifth number.")
            break
    except ValueError:
        print("Invalid value. Please, try again.")
        print("\n")
        continue
