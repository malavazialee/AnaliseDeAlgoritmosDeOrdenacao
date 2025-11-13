def bubbleSortComplexo(arr):
    """
    Bubble Sort melhorado - verifica se já está ordenado
    Melhor caso: O(n) quando array já está ordenado
    Pior caso: O(n²) quando array está em ordem inversa
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # Flag para verificar se houve trocas
        trocou = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        
        # Se não houve trocas, o array já está ordenado
        if not trocou:
            break
    
    return arr

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", teste)
    resultado = bubbleSortComplexo(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))