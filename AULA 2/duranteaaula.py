string1 = 'Oi!'
string2 = 'Oi, tudo bem?'
string3 = 'Ctrl+Play - escola de programação e robótica'
print(string1)
print(string2)
print(string3)
print("teste")
'teste' # não funciona

print("Saltando \nlinhas\n!") #quebra de linha
print('Olá! \t Ctrl+Play!') #espaçamento

#FUNÇÃO LEN
frase = "Ctrl+Play - Escola de programação e robótica"
print(len(frase)) #Começa no 1

#INDEXAÇÃO EM STRINGS
nome = "Fulano da Silva Sauro"
print(nome[7:]) #O caractere solicitado sempre é incluso se for no inicio!
print(nome[:7]) #Do inicio até o 6 caractere. Não inclui o 7.
print(nome[10:15]) #Do 10 incluso, até o 15 não incluso!
print(nome[-1]) #O último caractere será impresso.
print(nome[:-1]) #Do primeiro até o penúltimo (último não incluso)
print(nome[::2]) #Do primeiro caractére(índice 0) até o último(incluso) pulando um caractére
print(nome[1:10:2]) #Do segundo caractére(indice 1) até o décimo(não incluso) pulando um caractére

#FUNÇÃO FIND()
email = "fulano@ctrlplay.com.br"
print(email.find(".")) #mostra a posição do arroba

#FUNÇÃO COUNT()
print(email.count("."))

#IMUTABILIDADE DE STRING
teste = "imutabilidade"
teste[0] = "m" #Ocorrera um erro pois strings são imutáveis.
#CONCATENAÇÃO E REPETIÇÃO
nome = "José"
sobrenome = " Bond"
print(nome + sobrenome)
print(sobrenome * 7)

#FUNÇÃO STR()
#número não podem ser concatenados com string
numeroDeIrmaos = 2
#use a função str() para transformar numeros em strings
print('Você tem ' + str(numeroDeIrmaos) + " irmãos")
print('Você tem ' + numeroDeIrmaos + " irmãos") #destá forma ocorrerá um erro.

#MÉTODOS EMBUTIDOS EM STRINGS
exemplo = "Ctrl+Play - Escola de Programação e Robótica"
print(exemplo.upper()) #maiúsculo
print(exemplo.lower()) #minúsculo
#divide as strings nos espaços em branco:
cadaPalavra = exemplo.split() #não é possível passar por parâmetro a quantidade dos espaços, por isso criamos outra variável
print(cadaPalavra[2]) #Mostrará apenas a próxima palavra entre o segundo espaço e o terceiro.
cadaPalavra = exemplo.split('-') #Mostrará tudo entre um hífen e outro (como só tem um, mostra o resto da frase)
print(cadaPalavra[1]) #Se só houver um caractere deste tipo, é preciso passar por parametro [1]

#ENTRADA DE DADOS
nome = input("Digite seu nome: ")
print('\nOlá '+nome)    