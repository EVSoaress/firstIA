secreto = 'perfume'
"""
a palvra está fixa na variavel "secreto", mas para criar uma entrada de dados da variavel 
basta colocar no lugar de 'perfume' -> input('Digite uma palavra para ser advinhada')

"""
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você pode digitar apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Boaa, a letra "{letra}", exista na palavra secreta')
    else:
        print(f'Que pena a letra "{letra}", não existe na palavra secreta')
        digitadas.pop()

    novoSecreto = ''
    for novaLetra in secreto:
        if novaLetra in digitadas:
            novoSecreto += novaLetra
        else:
            novoSecreto += '*'

    if novoSecreto == secreto:
        print(f'Que legal, Você Ganhou! A palavra Secreta era {novoSecreto}.')
        break
    else:
        print(f'A palavra secreta está assim: {novoSecreto}')

    if letra not in secreto:
        chances -= 1