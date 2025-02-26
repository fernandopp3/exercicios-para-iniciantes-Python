#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1= int(input("Digite sua primeira nota"))
n2 = int(input("Digite sua segunda nota"))
m = n1 + n2
media = m/2
print("Sua média será {}".format(media))
if(media>=70):
    print("Parabéns, você foi aprovado")
else:
    print("Você foi reprovado.")
