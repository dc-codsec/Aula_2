"""
Python possui variáveis dinâmicas e fortes
Dinâmicas pois não precisamos declarar qual o tipo
da variável.
Forte pois não conseguimos fazer operações entre tipos
diferentes
Dai o Type Casting, a conversão de uma variável 
em outro tipo
"""

'''
str() converte em string
int() converte em inteiros
float() converte em float
'''
disco = 1000
disco_2 = "2000" #tipo str texto

total = disco + int(disco_2) #convertendo o str em int para somar
print(total)


print(str(disco) + disco_2) #convertendo o inteiro em str para concatenar

#convertendo um float em int
#somente a parte inteira restará
x = 10.6
print(x)
y = int(x)
print(y)

#A conversão de float em int não faz arredondamentos
# para arredondar um número utilizamos a função round
x = round(x)
print(x)