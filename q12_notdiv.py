# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

# Change the program for calculating prime numbers, informing, if the number is not prime, by which number it is divisible.

num = int(input("Enter a number: "))
cont = 0
list = []
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        list.append(i)
print('{} is divisible by {}.'.format(num,list,end=''))
if cont == 2:
    print('The number entered is a prime.')
else:
    print('The number entered is not a prime.')