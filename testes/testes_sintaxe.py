"""Arquivo de Testes Básicos de Sintaxe"""

#print(type(None))

'''
caracter = '1'
print('caracter é string:', type(caracter))

num = 1
print('num é int:', type(num))

numero = int(caracter)
print('numero é...?', type(numero))
'''

matriz = [['1', '2', '3'],['4', '5', '6']]
print(matriz)
print('====================')
print('lenght: ', len(matriz))
print('linha 0: ', matriz[0])
print('linha 1: ', matriz[1])
#print('linha 2: ', matriz[2])
print('====================')
print(matriz.__contains__('6'))
print(matriz.__contains__(['4', '5', '6']))
