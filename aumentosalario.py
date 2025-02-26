#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
satual = float(input("digite seu salário atual"))
sreajuste = satual + (satual * 15/100)
print("seu salário recebeu o aumento de 15%, ele ficará:{}".format(sreajuste))