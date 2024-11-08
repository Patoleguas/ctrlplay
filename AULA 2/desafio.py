frase = input(str('Digite uma frase: ')).upper()
espacoEmBranco = frase.count(' ')
print(f'existem {espacoEmBranco} espaços em branco!') #Maneira 1
print(f'existem {frase.count(' ')} espaços em branco!') #Maneira 2

vogalA = frase.count('A')
vogalE = frase.count('E')
vogalI = frase.count('I')
vogalO = frase.count('O')
vogalU = frase.count('U')
print(f'A vogal A, aparece {vogalA} vezes na frase!')
print(f'A vogal E, aparece {vogalE} vezes na frase!')
print(f'A vogal I, aparece {vogalI} vezes na frase!')
print(f'A vogal O, aparece {vogalO} vezes na frase!')
print(f'A vogal U, aparece {vogalU} vezes na frase!')
