#Exercício Python 005: Faça um programa que leia um número Inteiro
#  e mostre na tela o seu sucessor e seu antecessor
print('\033[35m Digite um numero que direi o Antecessor e o Sucessor \033[m')
numero=int(input('Digite um número : '))
print (' Você digitou o número ',numero)
print(f' O antecessor é {numero-1} e o Sucessor é {numero + 1}')