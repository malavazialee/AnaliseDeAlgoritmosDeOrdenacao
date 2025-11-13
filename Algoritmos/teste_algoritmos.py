from bubbleSortBasico import bubbleSortBasico
from bubbleSortComplexo import bubbleSortComplexo
from heapSort import heapSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSortPrimeiro import quickSortPrimeiro
from quickSortMedio import quickSortMedio
from selectionSort import selectionSort
from shellSort import shellSort

def testar_todos_algoritmos():
    """Testa todos os algoritmos com um array de exemplo"""
    print("=" * 60)
    print("TESTE DE TODOS OS ALGORITMOS DE ORDENACAO")
    print("=" * 60)
    
    # Array de teste
    teste = [64, 34, 25, 12, 22, 11, 90, 5, 77, 88, 3, 45]
    esperado = sorted(teste)
    
    print(f"Array original: {teste}")
    print(f"Array esperado: {esperado}")
    print()
    
    algoritmos = [
        ("Bubble Sort Basico", bubbleSortBasico),
        ("Bubble Sort Melhorado", bubbleSortComplexo),
        ("Insertion Sort", insertionSort),
        ("Selection Sort", selectionSort),
        ("Shell Sort", shellSort),
        ("Heap Sort", heapSort),
        ("Merge Sort", mergeSort),
        ("Quick Sort (Primeiro)", quickSortPrimeiro),
        ("Quick Sort (Central)", quickSortMedio)
    ]
    
    resultados = []
    
    for nome, algoritmo in algoritmos:
        try:
            resultado = algoritmo(teste)
            correto = resultado == esperado
            status = "✓ OK" if correto else "✗ ERRO"
            resultados.append((nome, status, correto))
            
            print(f"{nome:<25} {status}")
            if not correto:
                print(f"  Resultado: {resultado}")
                print(f"  Esperado:  {esperado}")
                
        except Exception as e:
            resultados.append((nome, f"✗ EXCEÇÃO: {e}", False))
            print(f"{nome:<25} ✗ EXCEÇÃO: {e}")
    
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    sucessos = sum(1 for _, _, correto in resultados if correto)
    total = len(algoritmos)
    
    print(f"Algoritmos testados: {total}")
    print(f"Algoritmos com sucesso: {sucessos}")
    print(f"Taxa de sucesso: {(sucessos/total)*100:.1f}%")
    
    if sucessos == total:
        print("\nTODOS OS ALGORITMOS FUNCIONAM CORRETAMENTE!")
    else:
        print(f"\n{total - sucessos} algoritmo(s) com problemas")
    
    return sucessos == total

def testar_casos_especificos():
    """Testa casos específicos como arrays vazios, unitários, etc."""
    print("\n" + "=" * 60)
    print("TESTE DE CASOS ESPECIFICOS")
    print("=" * 60)
    
    casos = [
        ("Array vazio", []),
        ("Array unitário", [5]),
        ("Array já ordenado", [1, 2, 3, 4, 5]),
        ("Array ordem inversa", [5, 4, 3, 2, 1]),
        ("Array com repetidos", [3, 1, 4, 1, 5, 9, 2, 6, 5]),
        ("Array com negativos", [5, -2, 7, -8, 0, -1, 3])
    ]
    
    algoritmos = [
        ("Bubble Sort Basico", bubbleSortBasico),
        ("Bubble Sort Melhorado", bubbleSortComplexo),
        ("Insertion Sort", insertionSort),
        ("Selection Sort", selectionSort),
        ("Shell Sort", shellSort),
        ("Heap Sort", heapSort),
        ("Merge Sort", mergeSort),
        ("Quick Sort (Primeiro)", quickSortPrimeiro),
        ("Quick Sort (Central)", quickSortMedio)
    ]
    
    todos_corretos = True
    
    for caso_nome, array in casos:
        print(f"\n{caso_nome}: {array}")
        esperado = sorted(array)
        
        for nome, algoritmo in algoritmos:
            try:
                resultado = algoritmo(array)
                if resultado == esperado:
                    print(f"  {nome:<25} ✓")
                else:
                    print(f"  {nome:<25} ✗")
                    print(f"    Resultado: {resultado}")
                    print(f"    Esperado:  {esperado}")
                    todos_corretos = False
            except Exception as e:
                print(f"  {nome:<25} ✗ EXCEÇÃO: {e}")
                todos_corretos = False
    
    return todos_corretos

if __name__ == "__main__":
    print("INICIANDO TESTES COMPLETOS DOS ALGORITMOS")
    print()
    
    # Testar algoritmo principal
    teste_principal_ok = testar_todos_algoritmos()
    
    # Testar casos específicos
    casos_especificos_ok = testar_casos_especificos()
    
    print("\n" + "=" * 60)
    print("RESULTADO FINAL DOS TESTES")
    print("=" * 60)
    
    if teste_principal_ok and casos_especificos_ok:
        print("TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("Os algoritmos estão prontos para o benchmark.")
    else:
        print("Alguns testes falharam. Verifique os algoritmos.")
        
    print("\nPróximo passo: Execute 'executar_tudo.py' para rodar o benchmark completo")