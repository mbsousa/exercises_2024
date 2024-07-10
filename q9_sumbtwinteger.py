

a = int(input("First number: "))
b = int(input("First nunmber: "))
cont = 0
list = []
for i in range(a,b+1):
    list.append(i)
    cont += i
print('The list between {} and {} is: {}.'.format(a,b,list))
print('The sum between the numbers is: {}'.format(cont))
