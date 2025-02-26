#Algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input("Digite o preço do prduto: R$"))
novo = preço - (preço * 5 / 100)
print("O valor com desconto ficará:{:.2f}".format(novo))
