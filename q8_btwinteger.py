# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# Write a program that receives two integers and generates the integers that are in the range comprised by them.

a = int(input("First number: "))
b = int(input("Second number: "))
print(f"The interval between {a} and {b} is: ")
list = []
for i in range(a,b+1):
    list.append(i)
print(list, end='')
