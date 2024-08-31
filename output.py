ip = input("Qual o seu IP? ")
nome = input("Qual é o seu nome? ")
mensagem = f'''
------------------
Olá {nome}
Seu ip é: {ip}
-------\t-----------
'''
print(mensagem)

nova_msg = "Olá usuário \n Seu IP é %s"%(ip) #format
nova_msg = "Olá usuário \n Seu IP é {0:s}".format(ip) #format
nova_msg = f"Olá \"usuário\" \n Seu IP é {ip}"
print(nova_msg)

x = "Valor {0:4.2f}".format(1500.4) 
print(x)

print(type(x))