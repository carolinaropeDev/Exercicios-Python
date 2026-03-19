#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considerando o dólar a R$5,24
valor= float(input('Quanto dinheiro você tem na carteira ?: R$ '))
conv= valor / 5.24
print(f'Com R${valor:.2f} Reais Você pode comprar ${conv:.2f} Dólares')