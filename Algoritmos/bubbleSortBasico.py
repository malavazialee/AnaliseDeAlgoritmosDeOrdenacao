def bubbleSortBasico(arr):
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        # Últimos i elementos já estão no lugar
        for j in range(0, n - i - 1):
            # Troca se o elemento encontrado for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Teste básico
if __name__ == "__main__":
    # Teste com array pequeno para verificação
    teste = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", teste)
    resultado = bubbleSortBasico(teste)
    print("Array ordenado:", resultado)
    print("Esta ordenado?", resultado == sorted(teste))