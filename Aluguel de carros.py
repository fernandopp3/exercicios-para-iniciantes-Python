#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.#

qtdkm = float(input("Digite a quantidade de km percorrido com o carro"))
qtddia = float(input("Digite a quantidade de dias que ficou com o carro"))
valordia = float(60 * qtddia)
valorkm = float(0.15 * qtdkm)
valortotal = valordia + valorkm
print("A divida da diária será de: {} \n A divida dos kms rodados será de: {}\n você deverá pagar {} reais".format(valordia, valorkm, valortotal))