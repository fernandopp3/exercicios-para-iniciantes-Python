#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
opção = input("Qual tipo você quer converter? \n A)Fahrenheit \n B)Graus Celcius \n Digite aqui:")

if opção == "A" or "b":
        fahrenheit = float(input("Digite o valor em graus fahrenheit aqui: "))
        resultado1 = (fahrenheit - 32) * 5/920
        print("A conversão de{} fahrenheit será para {:.2f} graus celcius ".format(fahrenheit, resultado1))

elif opção == "B" or opção == "b":
            graus = float(input("Digite o valor em graus celcius aqui: "))
            resultado2 = (graus * 9/5 + 32)
            print("A Conversão de{} graus vai para {}fahrenheit".form(graus, resultado2))

else: 
     print("Erro, essa opção é inválida")