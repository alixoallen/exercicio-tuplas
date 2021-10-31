numero=('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze', 'treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numer = int(input('Digite um numero de 0 a 20: '))
while numer < 0 or numer > 20:
    numer = int(input('Errou. Digite um número entre 0 e 20 -> '))
print(f'Você digitou o numero {numero[numer]}!')