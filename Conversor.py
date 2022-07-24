from QuadroOperacoes import *

#Operações
print(quadro)

question = str(input('Você ira usar qual operação? '))
valor = float(input('Qual valor sera usado? '))

#Multiplicação    
if question == 'Multiplicação':
    multiplicacao = float(input('Por quanto quer multiplicar?'))
    print('o valor é aproximadamente: ', valor * multiplicacao)

#Divisão    
if question == 'Divisão':
    divisao = float(input('Por quanto quer dividir? ')) 
    print('O valor aproximado da divisão é: ', valor / divisao)
    
#Adição 
if question == 'Adição':   
    adicao = float(input('Por quanto quer somar? '))
    print('O valor aproximado da soma é: ', valor + adicao)
    
#Subtração
if question == 'Subtração':
    subtracao = float(input('Por quanto quer subtrair? '))
    print('O valor aproximado da subtração é: ', valor - subtracao)
    
#Exponenciação
if question == 'Exponenciação':
    exponenciacao = float(input(f'Quer elevar {valor} a quanto? ')) 
    print('O valor aproximado da exponenciação é: ', valor ** exponenciacao)
    
#Resto divisão
if question == 'Resto da divisão':
    resto_divisao = float(input(f'Quer dividir {valor} por quanto? '))
    print('O valor aproximado do resto da divisão é: ', valor % resto_divisao)    
       
    
    

