#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite sua cidade: ")).strip() #Remove os espaçamentos desnecessários
print(cidade[:5].upper() == "SANTO")  #Verifica se os 5 primeiros caracteres são SANTO