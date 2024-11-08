nome = input(str('Digite seu nome: '))
partesNome = nome.split()
print(partesNome[0])
print(partesNome[1])
print(partesNome[-1])

#caso queiramos o sobrenome completo:
sobrenomeCompleto = " ".join(partesNome[1:])
print(sobrenomeCompleto)