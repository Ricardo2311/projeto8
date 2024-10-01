import random
import string
nome = input('Digite seu nome para inicar o programa: ')
comprimento = int(input('Digite o comprimento da senha: '))
caracteres = 0
maiuscula = input('Deseja utilizar letras maiúsculas(s/n): ')
if maiuscula == 's':
    caracteres = string.ascii_uppercase
else:
    caracteres = caracteres
minuscula = input('Deseja utilizar letras minúscula(s/n): ')
if minuscula == 's':
    caracteres = caracteres + string.ascii_lowercase
else:
    caracteres = caracteres
numeros = input('Deseja utilizar números(s/n): ')
if numeros == 's':
    caracteres = caracteres + string.digits
else:
    caracteres = caracteres
simbolos = input('Deseja utilizar simbolos(s/n): ')
if simbolos == 's':
    caracteres = caracteres + string.punctuation
else:
    caracteres = caracteres

senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

print(f'Atenção {nome}, a senha gerada foi: {senha}')
