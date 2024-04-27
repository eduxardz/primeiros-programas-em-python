"""Escreva um programa que receba uma string do usuário e remova todas as vogais dela."""

user = input('Digite uma frase: ')
vogais = str.maketrans('', '', 'a''e''i''o''u')
user = user.translate(vogais)
print(user)

