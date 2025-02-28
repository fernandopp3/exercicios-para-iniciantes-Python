# como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

#Biblioteca math: já vem acoplada no python com diversas funcionalidades, porém pussui algumas funcionalidades extras:
#Ceil para arredondar numeros para cima
#floor arredonda numeros para baixo
#Trunk trunkar numeros (Elimina da virgula para frente)
#pow(para potencia)
#sqrt calcular raiz quadrada
#factorial calcula o fatorial de um numero
#Para importar funcionalidades especificas deve-se digitar : from math import sqrt(Exemplo) ao invés de import math

import math
num = int(input("digite um numero:"))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))