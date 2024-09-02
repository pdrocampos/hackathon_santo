print("---------------EXERCISE 3---------------")
#Entrada com o valor do tamanho do array
size = int(input("Enter array size value: "))

#inicializa o array
array = []

#Preenche o array
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

#Função para retornar os subconjuntos
def generate_subsets(arr):
    subsets = [[]]
    
    #Para cada 1 no array cria novos subconjuntos 
    for i in arr:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [i])
        
        #Adiciona os subconjuntos a lista de subconjuntos
        subsets.extend(new_subsets)
    
    return subsets

#Chamada da Função
result = generate_subsets(array)
print("All subsets:", result)