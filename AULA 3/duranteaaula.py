convidados = ["José","Lucas","Ana","Enzo"]
convidadoRemovido = convidados.pop(0)
viajando = "Ana"
convidados.remove(viajando)
print(convidadoRemovido)
print(convidados)
convidados[0] = "Beatriz"
convidados.insert(0, "João")
convidados.append("Joaquim")
print("Primeiro convidado da festa: "+ convidados[-2])
print(convidados)
del convidados[3]
print(convidados)