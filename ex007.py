#Exercício Python 007: Desenvolva um programa que leia 
# as duas notas de um aluno, calcule e mostre a sua média.
nome_escola= 'Escola Cora Coralina'
print(f' \033[1;35m{nome_escola:^40}\033[m')
print('-'* 45)
print('Insira suas notas de Exatas e Humanas \nque irei calcular se você está de \033[31mRecuperação\033[m ou se foi \033[32mAprovado\033[m')
print('-'* 75)
nota1 = float(input('Insira sua nota de Humanas : '))
nota2 = float(input(' Insira sua nota de Exatas : '))
print(f'A sua média é {(nota1+nota2)/2:.2f}')
#PROXIMO PASSO PARA DESCOBRIR SE FOI APROVADO OU REPROVADO
#  NO EXERCICIO 40 EXERCICIOS DE IF ELIF