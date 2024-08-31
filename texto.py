"""
A classe Str string como objeto
possui vários métodos que podemos
utilizar para transformar o texto
atribuido a uma variavel
"""

url = "http://www.google.com.br"

'''
uniform resource locator 
schema: http, ftp:// smtp://
dominio: google.com.br
'''

#Um metodo str para colocar em maiuscula a primeira letra
url = url.capitalize()
print(url)

#método str para contar a ocorrência de uma determinada substring
#Atenção para o retorno de um inteiro como resposta
url = url.count(".")
print(url)

#métodos removeprefix e removesuffix para encontrar str no inicio/fim e remove-la
url = url.removeprefix("Http://")
print(url.removesuffix("com.br"))

#método replace para encontrar as ocorrencias do primeiro parametro e troca-las pelo segundo
print(url.replace("www", "#"))