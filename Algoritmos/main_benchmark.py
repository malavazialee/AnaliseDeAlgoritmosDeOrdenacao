import time
import random
import csv
import sys
from datetime import datetime

# Importar todos os algoritmos
from bubbleSortBasico import bubbleSortBasico
from bubbleSortComplexo import bubbleSortComplexo
from heapSort import heapSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSortPrimeiro import quickSortPrimeiro
from quickSortMedio import quickSortMedio
from selectionSort import selectionSort
from shellSort import shellSort

class BenchmarkOrdenacao:
    def __init__(self):
        self.algoritmos = {
            'Bubble Sort Basico': bubbleSortBasico,
            'Bubble Sort Melhorado': bubbleSortComplexo,
            'Insertion Sort': insertionSort,
            'Selection Sort': selectionSort,
            'Shell Sort': shellSort,
            'Heap Sort': heapSort,
            'Merge Sort': mergeSort,
            'Quick Sort (Primeiro)': quickSortPrimeiro,
            'Quick Sort (Central)': quickSortMedio
        }
        
        self.tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
        self.tipos_entrada = ['Aleatorio', 'Crescente', 'Decrescente']
        
    def gerar_aleatorio(self, n):
        return [random.randint(1, n * 10) for _ in range(n)]

    def gerar_crescente(self, n):
        return list(range(1, n + 1))

    def gerar_decrescente(self, n):
        return list(range(n, 0, -1))

    def verificar_ordenado(self, resultado):
        """Verifica se o array está corretamente ordenado"""
        for i in range(len(resultado) - 1):
            if resultado[i] > resultado[i + 1]:
                return False
        return True

    def determinar_repeticoes(self, tamanho):
        """Determina o número de repetições baseado no tamanho"""
        if tamanho <= 5000:
            return 5
        elif tamanho <= 20000:
            return 3
        else:
            return 2

    def mostrar_barra_progresso(self, progresso, total, largura=40):
        """Mostra barra de progresso no terminal"""
        percentual = progresso / total
        barras_preenchidas = int(largura * percentual)
        barras_vazias = largura - barras_preenchidas
        barra = '[' + '=' * barras_preenchidas + ' ' * barras_vazias + ']'
        percentual_texto = f'{percentual:.1%}'
        
        sys.stdout.write(f'\r{barra} {percentual_texto} ({progresso}/{total})')
        sys.stdout.flush()

    def testar_algoritmo(self, algoritmo, vetor_original):
        """Testa um algoritmo e retorna o tempo de execução"""
        try:
            # Fazer cópia para não alterar o vetor original
            vetor = vetor_original.copy()
            
            inicio = time.perf_counter()
            resultado = algoritmo(vetor)
            fim = time.perf_counter()
            
            # Verificar se está ordenado corretamente
            if not self.verificar_ordenado(resultado):
                return float('inf')
            
            return fim - inicio
            
        except Exception as e:
            return float('inf')

    def executar_benchmark_completo(self):
        """Executa o benchmark completo para todos os algoritmos"""
        resultados = []
        total_algoritmos = len(self.algoritmos)
        total_tamanhos = len(self.tamanhos)
        total_tipos = len(self.tipos_entrada)
        
        # Calcular total de testes
        total_testes = 0
        for tamanho in self.tamanhos:
            repeticoes = self.determinar_repeticoes(tamanho)
            total_testes += total_algoritmos * total_tipos * repeticoes
        
        print("INICIANDO BENCHMARK COMPLETO")
        print("=" * 60)
        print(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total de algoritmos: {total_algoritmos}")
        print(f"Total de tamanhos: {total_tamanhos}")
        print(f"Total de tipos de entrada: {total_tipos}")
        print(f"Total estimado de testes: {total_testes}")
        print("=" * 60)
        
        inicio_geral = time.time()
        teste_atual = 0
        
        for idx, (nome_algoritmo, algoritmo) in enumerate(self.algoritmos.items()):
            print(f"\n{nome_algoritmo} ({idx+1}/{total_algoritmos})")
            print("-" * 50)
            
            for tamanho in self.tamanhos:
                repeticoes = self.determinar_repeticoes(tamanho)
                
                for tipo in self.tipos_entrada:
                    # Gerar vetor conforme tipo
                    if tipo == 'Aleatorio':
                        vetor = self.gerar_aleatorio(tamanho)
                    elif tipo == 'Crescente':
                        vetor = self.gerar_crescente(tamanho)
                    else:  # Decrescente
                        vetor = self.gerar_decrescente(tamanho)
                    
                    tempos = []
                    sucessos = 0
                    
                    for rep in range(repeticoes):
                        teste_atual += 1
                        
                        tempo = self.testar_algoritmo(algoritmo, vetor)
                        if tempo != float('inf'):
                            tempos.append(tempo)
                            sucessos += 1
                    
                    # Calcular tempo médio
                    if tempos:
                        tempo_medio = sum(tempos) / len(tempos)
                        status = f"{tempo_medio:.4f}s"
                    else:
                        tempo_medio = float('inf')
                        status = "ERRO"
                    
                    resultados.append({
                        'Algoritmo': nome_algoritmo,
                        'Tamanho': tamanho,
                        'Tipo_Entrada': tipo,
                        'Tempo_Medio': tempo_medio,
                        'Repeticoes': repeticoes,
                        'Sucessos': sucessos
                    })
                    
                    print(f"   {tipo} - Tamanho {tamanho}: {status} ({sucessos}/{repeticoes} ok)")

        tempo_total = time.time() - inicio_geral
        print(f"\n" + "=" * 60)
        print(f"BENCHMARK CONCLUIDO!")
        print(f"Tempo total: {tempo_total/60:.1f} minutos")
        print(f"Testes executados: {teste_atual}")
        print(f"Fim: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        return resultados

    def salvar_resultados(self, resultados):
        """Salva os resultados em arquivo CSV"""
        with open('resultados_benchmark_completo.csv', 'w', newline='', encoding='utf-8') as f:
            campos = ['Algoritmo', 'Tamanho', 'Tipo_Entrada', 'Tempo_Medio', 'Repeticoes', 'Sucessos']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for r in resultados:
                writer.writerow(r)
        
        print("Resultados salvos em 'resultados_benchmark_completo.csv'")

# Execução direta do arquivo
if __name__ == "__main__":
    print("BENCHMARK INDIVIDUAL - ALGORITMOS DE ORDENACAO")
    print(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Aviso sobre tempo de execução
    print("AVISO: Este benchmark pode demorar varios minutos")
    
    confirmacao = input("Deseja continuar? (s/n): ").lower()
    if confirmacao != 's':
        print("Execucao cancelada.")
        exit()
    
    # Executar benchmark
    inicio_geral = time.time()
    
    benchmark = BenchmarkOrdenacao()
    resultados = benchmark.executar_benchmark_completo()
    benchmark.salvar_resultados(resultados)
    
    tempo_total = time.time() - inicio_geral
    print(f"\nPROCESSO CONCLUIDO!")
    print(f"Tempo total: {tempo_total/60:.2f} minutos")