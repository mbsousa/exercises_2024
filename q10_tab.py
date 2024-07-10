# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.

# Develop a multiplication table generator, capable of generating the multiplication table of any integer between 1 and 10.
# The user must inform which number he wants to see the multiplication table for.

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        list = [1,2,3,4,5,6,7,8,9,10]
        if num in list:
            for i in range(1,10+1):
                print('{} x {} = {}'.format(num,i,num*i))
        else:
            print("Please, enter a number between 1 and 10.")
    except ValueError:
        print("Invalid number.")