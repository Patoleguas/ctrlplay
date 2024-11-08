num_funcionario = int(input('Digite o número do seu crachá: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
valor_hora = float(input('Digite o valor do seu salário por hora: R$ '))

calculo_salario = valor_hora * horas_trabalhadas

print(f"O número do seu crachá é {num_funcionario} e o seu salário esse mês é de R$ {calculo_salario}")