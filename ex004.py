#Faça um programa que leia algo pelo teclado e mostre na tela
#  o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('Digite algo : ')
print('O tipo primitivo desse valor é  ', type(algo))
print ('Tem apenas letras ?',algo.isalpha())
print('So tem espaço? ',algo.isspace())
print('É somente números ?', algo.isnumeric())
print ('Tem letras e números ?',algo.isalnum())
print ('Tem apenas letras Maiúsculas ?', algo.isupper())
print ('Tem apenas letras minusculas ?',algo.islower())
print ('Tem Titulo ? (letras maiúsculas no começo de cada palavra)', algo.istitle())