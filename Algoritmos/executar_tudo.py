import os
import sys
import time
from datetime import datetime

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("Verificando dependencias...")
    try:
        import matplotlib
        import pandas
        import numpy
        print("Todas as dependencias estao instaladas!")
        return True
    except ImportError as e:
        print(f"Erro: {e}")
        print("Instale as dependencias com: pip install matplotlib pandas numpy")
        return False

def verificar_resultados_existem():
    """Verifica se os resultados do benchmark já existem"""
    return os.path.exists('resultados_benchmark_completo.csv')

def verificar_graficos_existem():
    """Verifica se a pasta de gráficos existe e tem arquivos"""
    pasta_graficos = "graficos_benchmark"
    if not os.path.exists(pasta_graficos):
        return False
    
    arquivos_graficos = os.listdir(pasta_graficos)
    return len(arquivos_graficos) >= 10  # Número mínimo de gráficos esperados

def executar_benchmark():
    """Executa o benchmark completo"""
    print("\n" + "="*60)
    print("EXECUTANDO BENCHMARK COMPLETO")
    print("ESTE PROCESSO PODE DEMORAR VÁRIOS MINUTOS")
    print("="*60)
    
    try:
        from main_benchmark import BenchmarkOrdenacao
        benchmark = BenchmarkOrdenacao()
        resultados = benchmark.executar_benchmark_completo()
        benchmark.salvar_resultados(resultados)
        return True
    except Exception as e:
        print(f"Erro ao executar benchmark: {e}")
        return False

def gerar_graficos():
    """Gera todos os gráficos"""
    print("\n" + "="*60)
    print("GERANDO GRAFICOS E RELATORIOS")
    print("="*60)
    
    try:
        from gerador_graficos_completo import GeradorGraficos
        gerador = GeradorGraficos()
        df = gerador.carregar_dados()
        gerador.gerar_relatorio_completo(df)
        return True
    except Exception as e:
        print(f"Erro ao gerar graficos: {e}")
        return False

def main():
    print("SISTEMA COMPLETO DE BENCHMARK - ALGORITMOS DE ORDENACAO")
    print(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Verificar dependências
    if not verificar_dependencias():
        print("Dependencias faltando. Instale-as primeiro.")
        return
    
    # Verificar se resultados já existem
    resultados_existem = verificar_resultados_existem()
    graficos_existem = verificar_graficos_existem()
    
    if resultados_existem:
        print("Resultados do benchmark encontrados")
    else:
        print("Resultados do benchmark nao encontrados")
    
    if graficos_existem:
        print("Graficos encontrados")
    else:
        print("Graficos nao encontrados")
    
    print("\nOPCOES:")
    print("1. Executar TUDO (benchmark + graficos + analise)")
    print("2. Apenas gerar graficos (se resultados existirem)")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opcao (1-3): ").strip()
    
    if opcao == "1":
        # Aviso sobre tempo de execução
        print("\nAVISO: Este benchmark executara mais de 2.000 testes")
        print("Tempo estimado: 10-30 minutos dependendo do hardware")
        
        confirmacao = input("Deseja continuar? (s/n): ").lower()
        if confirmacao != 's':
            print("Execucao cancelada.")
            return
        
        # Executar benchmark completo
        inicio_geral = time.time()
        
        if executar_benchmark():
            gerar_graficos()
            
            tempo_total = time.time() - inicio_geral
            print(f"\nPROCESSO CONCLUIDO!")
            print(f"Tempo total: {tempo_total/60:.2f} minutos")
            print(f"Fim: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    elif opcao == "2":
        if not resultados_existem:
            print("Erro: Resultados do benchmark nao encontrados.")
            print("Execute primeiro a opcao 1 para gerar os resultados.")
            return
        gerar_graficos()
        
    elif opcao == "3":
        print("Saindo...")
        return
        
    else:
        print("Opcao invalida!")

if __name__ == "__main__":
    main()