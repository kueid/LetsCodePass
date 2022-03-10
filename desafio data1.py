def pega_chave(val, dict):
    for chave, valor in dict.items():
        if val == valor:
            return chave

    return "sem chave"


esquema = {'_': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
           'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
           'w': 23, 'x': 24, 'y': 25, 'z': 26, '.': 27}
chave_secreta_k = 0
textoplano = ''
textocifrado = []
cifradocodigo = []
codigoplano = []
opc = int(input('opção: '))

while True:
    if opc == 1:
        chave_secreta_k = int(input('digite o numero da chave secreta: '))
        textoplano = input('digite o texto pra cifrar: ')
        for letra in textoplano:
            codigoplano.append(esquema[letra])

        for i, num in enumerate(codigoplano):
            cifradocodigo.append((codigoplano[(chave_secreta_k * i) % len(codigoplano)] - i) % 28)

        for i in cifradocodigo:
            textocifrado.append(pega_chave(i, esquema))

        print(''.join(textocifrado))
        break
    if opc == 2:
        chave_secreta_k = int(input('digite o numero da chave secreta: '))
        textoplano = input('digite o texto pra descifrar: ')

        for letra in textoplano:
            codigoplano.append(esquema[letra])
            cifradocodigo.append(0)

        for i, num in enumerate(codigoplano):
            cifradocodigo[(chave_secreta_k * i) % len(codigoplano)] = ((codigoplano[i] + i) % 28)

        for i in cifradocodigo:
            textocifrado.append(pega_chave(i, esquema))

        print(''.join(textocifrado))

        break
    if opc != 2 or 1:
        opc = int(input('opção: '))
        continue
