def shellSort(arr):
    """
    Shell Sort - variação do Insertion Sort com gaps
    Complexidade: O(n log n) a O(n²) dependendo da sequência de gaps
    """
    arr = arr.copy()
    n = len(arr)
    
    # Sequência de gaps (usando sequência de Shell)
    gap = n // 2
    
    while gap > 0:
        # Faz insertion sort para este gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Desloca elementos até encontrar a posição correta
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        # Reduz o gap
        gap //= 2
    
    return arr

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90, 5, 77, 88]
    print("Array original:", teste)
    resultado = shellSort(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))