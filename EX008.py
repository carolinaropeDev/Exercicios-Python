#Exercício Python 008: Escreva um programa que leia um valor em metros 
# e o exiba convertido em centímetros e milímetros.
valor=float(input('Insira um valor em metros que darei a conversão : '))
cm = valor*100
mm= valor*1000
print(f'Você digitou {valor} metros \neste valor em centímetros é {cm:.2f} cm \n convertido em milimetros é {mm:.2f} milimetros ')