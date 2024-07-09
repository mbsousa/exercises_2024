# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

# Write a program that reads a username and password and does not accept the 
# password that is the same as the username, showing an error message and asking for the information again.

import getpass

while True:
    user = input("Your username: ")
    password = getpass.getpass("Your password: ")
    if password != user:
        print("Successfully registered.")
        break
    else:
        print("Username and password should not the same. Please, try again.")
        continue

