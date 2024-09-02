print("---------------EXERCISE 3---------------")

# Entrada com o valor do tamanho do array
size = int(input("Enter array size value: "))

# Inicializa o array
array = []

# Preenche o array
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# Função para retornar os subconjuntos
def generate_subsets(array, max_size=None, min_size=None, distinct_only=False, sort_subsets=False):
    if distinct_only:
        array = list(set(array))
    
    subsets = [[]]
    #Cria novos subconjuntos adicionando o elemento atual
    for i in array:
        subsets += [subset + [i] for subset in subsets]
    #Filtra subconjuntos que tenham pelo menos o tamanho mínimo
    if min_size is not None:
        subsets = [s for s in subsets if len(s) >= min_size]
    #Filtra subconjuntos que tenham no máximo o tamanho máximo    
    if max_size is not None:
        subsets = [s for s in subsets if len(s) <= max_size]
    #Ordena os elementos dentro dos subconjuntos e a lista de subconjuntos   
    if sort_subsets:
        subsets = [sorted(s) for s in subsets]
        subsets.sort()

    return subsets

# Entrada dos parâmetros opcionais
max_size = int(input("Enter max size (or press Enter to skip): ") or 0) or None
min_size = int(input("Enter min size (or press Enter to skip): ") or 0) or None
distinct_only = input("Distinct only (True/False)? ").lower() == 'true'
sort_subsets = input("Sort subsets (True/False)? ").lower() == 'true'

# Chamada da função
result = generate_subsets(array, max_size, min_size, distinct_only, sort_subsets)
print("All subsets:", result)