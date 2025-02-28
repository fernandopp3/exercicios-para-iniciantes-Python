#vamos aprender operações com String no Python. As principais operações que vamos aprender são
#o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), 
# lower(), capitalize(), title(), strip(), junção com join().

#frase.Lean vai  exibir o numero de caracteres de uma string

#frase.count("o") vai contar quantas vezes aparece a letra o dentro da string  & frase.count("o",0,13) realiza um fatiamento a partir do 13 caracter

#frase.find("deo") ele vai indicar em qual posição essas letras estão, podendo ser um letra só 
#Obs: se ele retornar -1 é pq a letra não existe

#"Curso in frase" ele vai retornar se essa palavra existe dentro da string

#frase.replace("Python","Android") esse comando irá substituir a palavra python por android dentro da string

#frase.upper() Ele vai converter todas as letras minusculas em maiúsculas, mantendo as que ja estavam maiusculas

#frase.lower() Ele converte as letras maiusculas para minusculas

#frase.capitalize() Vai pegar uma string inteira e jogar tudo para minúscula, enquanto vai transformar o primeiro caracter em maiuscula

#frase.title() Ele vai transformar todas as primeiras letras após um espaçamento em maiusculas, enquanto o restante fica minusculas

#frase.strip() Remove todos os espaçamentos desnecessários antes de inciar a frase e após o termino 
#frase.rtrip() Mesma coisa, removendo somente do lado direito
#frase.lstrip() Mesma coisa, removendo somente do lado esquero

#frase.split() Ele vai remover reiniciar a contágem de caracteres a cada espaçamento em branco dentro da frase-
#sendo assim, ele irá dividr a frase da string em subgrupos contando a partir de 0, e dentro desses grupos será
#contido em numeração os caracteres da frase

#"-".join(frase) vai substituir todos os espaçamentos dentro da string por "-"

frase = "Olá mundo, tudo beleza?"
print(frase.upper().count("0"))

print(len(frase.estrip()))

print(frase.replace("beleza", "Android"))

print(frase.lower().find("video"))

dividido = frase.split()
print(dividido[2][3])

#Para realizar uma atribuição (modificação fixa na string), se deve adicionar frase= (frase.replace("beleza",Android))