#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente. 

nome = str(input("Digite seu nome completo: ")).strip()

nome = nome.split()

print("Seu primeiro nome é: {} \n Seu ultimo nome é: {}".format(nome[0], nome[len(nome) -1]))

