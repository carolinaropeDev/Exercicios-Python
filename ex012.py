#Exercício Python 012: Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
valor = float(input('Insira o Preço do seu produto e direi o novo preço com desconto R$'))
valor_final = valor * 0.95
print(f'O seu produto custa R${valor:.2f} e com desconto de 5% ele ficará R${valor_final:.2f}.')