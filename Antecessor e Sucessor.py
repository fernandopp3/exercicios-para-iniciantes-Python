#Crie um programa que reconheça um numero e indique o antecessor e sucessor dele.
numero = int(input("Digite um numero:")) 
sucessor = numero + 1
antecessor = numero - 1
print("O sucessor de {} é {} e o antecessor é {}".format(numero, sucessor, antecessor))