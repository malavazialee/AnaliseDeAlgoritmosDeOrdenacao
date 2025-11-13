def heapSort(arr):
    """
    Heap Sort - usa estrutura de heap máximo
    Complexidade: O(n log n) em todos os casos
    """
    
    def heapify(arr, n, i):
        """
        Transforma a subárvore enraizada no índice i em um heap máximo
        """
        largest = i  # Inicializa o maior como raiz
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Verifica se o filho esquerdo existe e é maior que a raiz
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # Verifica se o filho direito existe e é maior que o maior até agora
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # Troca e continua heapificando se necessário
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    arr = arr.copy()
    n = len(arr)
    
    # Constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        # Move a raiz atual para o final
        arr[i], arr[0] = arr[0], arr[i]
        # Chama heapify na heap reduzida
        heapify(arr, i, 0)
    
    return arr

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90, 5, 77]
    print("Array original:", teste)
    resultado = heapSort(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))