def quickSortMedio(arr):
    """
    Quick Sort com pivô sendo o elemento central
    Melhor caso: O(n log n)
    Caso médio: O(n log n)
    Pior caso raro: O(n²)
    """
    
    def particionar(arr, inicio, fim):
        """
        Particiona o array usando o elemento do meio como pivô
        """
        meio = (inicio + fim) // 2
        pivo = arr[meio]
        
        # Move o pivô para o início
        arr[meio], arr[inicio] = arr[inicio], arr[meio]
        
        left = inicio + 1
        right = fim
        
        while left <= right:
            # Encontra elemento maior que o pivô
            while left <= right and arr[left] <= pivo:
                left += 1
            
            # Encontra elemento menor que o pivô
            while left <= right and arr[right] >= pivo:
                right -= 1
            
            # Troca os elementos se necessário
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
        
        # Coloca o pivô na posição correta
        arr[inicio], arr[right] = arr[right], arr[inicio]
        return right
    
    def quick_sort(arr, inicio, fim):
        if inicio < fim:
            # Encontra a posição do pivô
            pos = particionar(arr, inicio, fim)
            
            # Ordena recursivamente os subarrays
            quick_sort(arr, inicio, pos - 1)
            quick_sort(arr, pos + 1, fim)
    
    # Cria cópia para não modificar o original
    arr_copy = arr.copy()
    if len(arr_copy) <= 1:
        return arr_copy
    
    quick_sort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90, 5, 77]
    print("Array original:", teste)
    resultado = quickSortMedio(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))