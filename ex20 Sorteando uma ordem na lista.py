#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

n1 = str(input("aluno 1"))
n2 = str(input("aluno 2"))
n3 = str(input("aluno3"))
n4 = str(input("aluno 4"))
lista = [n1,n2,n3,n4]

random.shuffle(lista)
print("A ordem será:")
print(lista)