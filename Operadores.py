#Conhecendo todos os operadores 
n1 = int(input("Digite um numero:"))
n2 = int(input("Digite outro numero:"))
s = n1 + n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1**n2
sobra = n1%n2

print("A soma vale{},\n o produto é{}, \n e a divisão é{}\n".format(s, m, d))
print("Divisão inteira{},\n e potência{}\n".format(di, e))
print("Resto da divisão{}".format(sobra))