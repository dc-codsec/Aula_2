#Para interagirmos com o usuário e recebermos dados 
#através do teclado utilizamos a função input()
marca = input("Digite a marca da memoria: ")

#A função input retorna um valor string, logo 
#se o valor da resposta for numérico ou float
#temos que fazer a conversão
memoria = int(input("Qual a quantidade de memoria? "))
print(memoria)

memoria_nova = memoria + 2048
print("Nova memoria", memoria_nova)