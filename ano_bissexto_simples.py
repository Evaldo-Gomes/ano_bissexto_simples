#Ano Bissexto
#Apresentação
print('\n\t\t\t  --  Ano Bissexto   --')

#Entradas
n = int(input('Informe o ano: '))

#Processamento
if n % 4 == 0:
    print(f'O ano {n} é bissexto.')
else:
    print(f'O ano {n} não é bissexto.')
