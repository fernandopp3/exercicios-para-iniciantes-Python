#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math #Ou from math import hypot

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)
print("O comprimento da hipotenusa é:{} ".format(hipotenusa))

#Ou podemos importar hypot(calcula a hipotenusa com math)