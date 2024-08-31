'''
Uma variavel é utilizada para armazenarmos um dado 
utilizado em nosso script.
Para atribuir um valor a uma variavel
usamos o operador '=' 
Esse valor poderá ser alterado durante a execução do 
programa
'''
ip = "192.168.10.1" #ATRIBUINDO O VALOR A VARIAVEL
print(ip)
# O operador = é diferente dàquele da matemática 
# Aqui ele significa que o valor da direita está sendo atribuido
# ao valor da esquerda 

#CONSTANTES são valores que não podem ser alterados durante o script
#Em python essa funcionalidade não existe, porém há uma convenção
#de utilizarmos letras maiúsculas para identificar uma variável 
#que não deve ser alterada, "simulando uma constante"
PORTA = 80 
print(PORTA)

PORTA = 443
print(PORTA)

"""
Os nomes das variáveis em python
aceitam apenas: letras minusculas,maiusculas, números
e underline
a-zA-Z0-9_
Porém só podem começar com letras ou underline
"""
