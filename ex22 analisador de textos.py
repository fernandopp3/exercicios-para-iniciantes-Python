#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nom

nome = str(input("Digite seu nome")).strip() #strip ja vai eliminar os espaços antes e depois do fim da frase

print("Seu nome em minusculas é:{}".format(nome.upper()))
print("Seu nome em minusculas é:{}".format(nome.lower()))
print("Seu nome possui:{} caracteres".format(len(nome)-nome.count(" "))) #len vai contar o numero de caracéres e count vai deletar todos os espaçamentos
print("Seu primeiro nome possui {}letras".format(nome.find(" "))) #find vai ler até o primeiro espaçamento
