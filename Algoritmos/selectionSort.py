def selectionSort(arr):
    """
    Selection Sort - seleção direta
    Complexidade: O(n²) em todos os casos
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # Encontra o menor elemento no array não ordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", teste)
    resultado = selectionSort(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))