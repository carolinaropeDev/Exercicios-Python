#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
print('_'*15)
azul = '\033[34m'
limpacor = '\033[m'
print (f'{azul}' + 'TABUADA'.center(15) + f'{limpacor}')
print('_'*15)
numero = int(input('Digite um número e direi a tabuada '))
print(f'{numero} x  1 = {azul} {numero*1} {limpacor}')
print(f'{numero} x  2 = {azul} {numero*2} {limpacor}')
print(f'{numero} x  3 = {azul} {numero*3} {limpacor}')
print(f'{numero} x  4 = {azul} {numero*4} {limpacor}')
print(f'{numero} x  5 = {azul} {numero*5} {limpacor}')
print(f'{numero} x  6 = {azul} {numero*6} {limpacor}')
print(f'{numero} x  7 = {azul} {numero*7} {limpacor}')
print(f'{numero} x  8 = {azul} {numero*8} {limpacor}')
print(f'{numero} x  9 = {azul} {numero*9} {limpacor}')
print(f'{numero} x 10 = {azul} {numero*10} {limpacor}')
print('_'*15)