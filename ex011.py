#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Quantos metros sua parede tem de Largura?:'))
altura = float(input('Quantos metros tem Altura?:'))
area = largura * altura
tinta = area / 2
print (f'Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e a area dela é de {area:.2f}m²')
print(f'Para pintar sua parede será necessário {tinta:.2f}L de Tinta')