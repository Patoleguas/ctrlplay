montante = int(input('Digite um valor em dinheiro: R$ '))
meses = int(input('Digite o número de meses: '))

taxa_juros = 0.005 # equivalente à 0.5%

rendimento = montante * ((1 + taxa_juros) ** meses - 1) #formula do montante

print(f"O rendimento do montante após {meses} será de R$ {rendimento:.2f}")