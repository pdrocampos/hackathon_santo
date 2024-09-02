#SEGUE ABAIXO MINHA SOLUÇÃO PARA O DESAFIO 0 - EXERCICIO 2

print("---------------EXERCICIO 2---------------")
#Entrada com o valor do tamanho do array
size = int(input("Enter array size value: "))

#inicializa o array
array = []

#Preenche o array
for i in range(size):
    element = int(input("Enter element {i + 1}: "))
    array.append(element)

#Função para retornar os pares com menor valor absoluto
def absolute_diff(array):
    #Ordena o array
    array = sorted(array)
    #Inicialização das variaveis
    pairs = []
    min_diff = float('inf')

    #Percorre o array para achar os pares de menor diferença
    for i in range(len(array) - 1):
        a = array[i]
        b = array[i+1]
        diff = b - a
        #Quando achar a menor diferença redefine a lista
        if diff < min_diff: 
            min_diff = diff
            pairs = [[a,b]]
        #Se a diferença for igual a menor já encontrada, adiciona o par
        elif diff == min_diff: 
            pairs.append([a,b])

    return pairs

#Chama a função
result = absolute_diff(array)
print(result)