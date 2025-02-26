#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = int(input("digite o valor em metros"))
cm = m * 100
mm = m * 1000
print("Os {} metros foram convertidos em {} centimetros e {} milimetros".format(m, cm, mm))