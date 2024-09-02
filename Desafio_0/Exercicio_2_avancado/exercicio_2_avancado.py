print("---------------EXERCICIO 2 AVANÇADO---------------")

# Entrada com o valor do tamanho do array
size = int(input("Enter array size value: "))

# Inicializa o array
array = []

# Preenche o array
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# Função para retornar os pares com menor diferença absoluta
def absolute_diff(array, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    # Ordena o array
    array = sorted(array)
    
    # Inicialização das variáveis
    pairs = []
    min_diff = float('inf')

    # Percorre o array para achar os pares de menor diferença
    for i in range(len(array) - 1):
        a = array[i]
        b = array[i + 1]
        diff = b - a
        
        # Quando achar a menor diferença redefine a lista
        if diff < min_diff:
            min_diff = diff
            pairs = [[a, b]]
        # Se a diferença for igual à menor já encontrada, adiciona o par
        elif diff == min_diff:
            pairs.append([a, b])

    # Remove duplicatas caso allow_duplicates seja False
    if not allow_duplicates:
        pairs = [pair for pair in pairs if pair[0] != pair[1]]
    
    # Ordena os pares em ordem crescente se sorted_pairs for True
    if sorted_pairs:
        pairs = [sorted(pair) for pair in pairs]
    
    # Remove pares espelhados (a, b) e (b, a) se unique_pairs for True
    if unique_pairs:
        seen = set()
        unique = []
        for pair in pairs:
            sorted_pair = tuple(sorted(pair))
            if sorted_pair not in seen:
                seen.add(sorted_pair)
                unique.append(pair)
        pairs = unique

    return pairs

# Entrada dos parâmetros opcionais
allow_duplicates = input("Allow duplicates (True/False)? ").lower() == 'true'
sorted_pairs = input("Sort pairs (True/False)? ").lower() == 'true'
unique_pairs = input("Unique pairs (True/False)? ").lower() == 'true'

# Chama a função
result = absolute_diff(array, allow_duplicates, sorted_pairs, unique_pairs)
print(result)