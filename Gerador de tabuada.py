# Esse programa irá gerar a tabuada do número que você digitar

while True:
    try:
        numero_entrada = int(input('Digite um número: '))
        break  # Sai do loop se o número for válido
    except ValueError:
        print('Isso não é um número. Por favor, digite um número inteiro.')

tabuada = list(range(1, 11))  # Utilizo range para fazer uma lista de 1 a 10

for i in tabuada:
    print(f'{numero_entrada} x {i} = {i * numero_entrada}')
