#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última ve

frase = str(input("Digite uma frase: ")).strip()

frase = (frase.upper())

print("A letra A aparece {} vezes na frase".format((frase.count("A"))))
print("Ela aparece a primeira vez na posição {}".format((frase.find("A"))))
print("Ela aparece a ultima vez na posição {}".format((frase.rfind("A")))) #rfind procura a letra a patir do lado direitob