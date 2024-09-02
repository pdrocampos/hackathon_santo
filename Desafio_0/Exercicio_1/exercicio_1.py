#SEGUE ABAIXO MINHA SOLUÇÃO PARA O DESAFIO 0 - EXERCICIO 1

print("---------------EXERCICIO 1---------------")
#Entrada do valor de n 
n = int(input("Enter the value of n: "))

#Função que faz a geração da lista de asteriscos
def list(n):
    asterisks = []
    for i in range(1, n + 1):
        asterisks.append("*" * i)
    return asterisks

#Chamada da Função
resul = list(n) 

#Imprime o resultado
print(resul)             