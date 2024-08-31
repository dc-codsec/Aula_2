ip = input("Qual o seu IP? ")
nome = input("Qual é o seu nome? ")

#Podemos utilizar strings de várias formas
#A mais recente é através das f-strings
#Também podemos utilizar texto com 3 aspas
#simples ou duplas, assim como nos comentários
#e ao atribuirmos ele a uma variável temos uma
#string multilinha
mensagem = f'''
------------------
Olá {nome}
Seu ip é: {ip}
-------\t-----------
'''
print(mensagem)

#função format com operador %s p/string %d para interiro e %f para float
nova_msg = "Olá usuário \n Seu IP é %s"%(ip) 
nova_msg = "Olá usuário \n Seu IP é {0:s}".format(ip) #função format
nova_msg = f"Olá \"usuário\" \n Seu IP é {ip}" #f-string
print(nova_msg)

#É possível a formatação das strings 
x = "Valor {0:4.2f}".format(1500.4) 
print(x)
