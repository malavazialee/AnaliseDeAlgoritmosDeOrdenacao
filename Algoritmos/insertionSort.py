def insertionSort(arr):
    """
    Insertion Sort - inserção direta
    Melhor caso: O(n) quando array já está ordenado
    Pior caso: O(n²) quando array está em ordem inversa
    Caso médio: O(n²)
    """
    arr = arr.copy()
    
    # Percorre do segundo elemento ao último
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento atual a ser inserido
        j = i - 1     # Índice do elemento anterior
        
        # Move elementos maiores que key uma posição à frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insere key na posição correta
        arr[j + 1] = key
    
    return arr

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", teste)
    resultado = insertionSort(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))