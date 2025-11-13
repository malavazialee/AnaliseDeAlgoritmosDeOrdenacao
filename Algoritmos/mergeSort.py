def mergeSort(arr):
    """
    Merge Sort - algoritmo de divisão e conquista
    Complexidade: O(n log n) em todos os casos
    """
    
    def merge(left, right):
        """
        Combina duas listas ordenadas em uma única lista ordenada
        """
        result = []
        i = j = 0
        
        # Combina as duas listas em ordem
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Adiciona os elementos restantes
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # Caso base: array com 0 ou 1 elemento já está ordenado
    if len(arr) <= 1:
        return arr.copy()
    
    # Divide o array no meio
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    # Combina as metades ordenadas
    return merge(left, right)

# Teste básico
if __name__ == "__main__":
    teste = [64, 34, 25, 12, 22, 11, 90, 5, 77, 88]
    print("Array original:", teste)
    resultado = mergeSort(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))