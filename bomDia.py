'''
Nome: Clarissa Cruz
Data: 29/10/2024
versão 1
'''

#Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. 
# Imprima a mensagem “Bom dia!” ou  “Boa Noite” ou “Valor inválido”, conforme o caso.  

turno = input('Digite M-matutino ou V-vespertino ou N-noturno: ') .strip().lower()

if turno == 'm':
    print ('Bom dia!')
elif turno == 'v':
    print ('Boa tarde!')
elif turno == 'n':
    print ('Boa Noite!') 
else:
    print ('Valor inválido')