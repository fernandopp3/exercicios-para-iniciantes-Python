#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input("Digite a largura da parede"))
altura = float(input("digite a altura da parede"))
mquadrado = largura * altura
print("Sua parede tem{} metros quadrados".format(mquadrado))
tinta = mquadrado / 2
print("Para pintar essa parede, você precisará de {}l de tinta".format(tinta))