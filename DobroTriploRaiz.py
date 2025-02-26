#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input("digite um numero: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} vale {} \n O triplo vale {}\n e a raiz quadrada é {}".format(n, d, t, r))