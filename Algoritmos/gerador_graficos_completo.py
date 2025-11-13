import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

class GeradorGraficos:
    def __init__(self):
        # Criar pasta para os gráficos
        self.pasta_graficos = "graficos_benchmark"
        self.criar_pasta_graficos()
        
        # Configurações de estilo
        plt.style.use('seaborn-v0_8')
        self.cores = plt.cm.Set3(np.linspace(0, 1, 12))
        
        # Configurações dos gráficos
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'DejaVu Sans'
    
    def criar_pasta_graficos(self):
        """Cria a pasta para salvar os gráficos"""
        if not os.path.exists(self.pasta_graficos):
            os.makedirs(self.pasta_graficos)
            print(f"Pasta '{self.pasta_graficos}' criada com sucesso!")
        else:
            print(f"Pasta '{self.pasta_graficos}' ja existe.")
    
    def carregar_dados(self, arquivo='resultados_benchmark_completo.csv'):
        """Carrega os dados do arquivo CSV"""
        try:
            df = pd.read_csv(arquivo)
            print(f"Dados carregados: {len(df)} registros")
            return df
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' nao encontrado!")
            print("Execute primeiro o main_benchmark.py")
            return None
    
    def salvar_grafico(self, nome):
        """Salva o gráfico atual na pasta"""
        caminho = os.path.join(self.pasta_graficos, nome)
        plt.savefig(caminho, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"Grafico salvo: {nome}")
    
    def gerar_graficos_individualmente(self, df):
        """Gera gráficos individuais para cada algoritmo"""
        print("\nGerando gráficos individuais...")
        
        algoritmos = df['Algoritmo'].unique()
        
        for algoritmo in algoritmos:
            plt.figure(figsize=(12, 8))
            dados_algoritmo = df[df['Algoritmo'] == algoritmo]
            
            for i, tipo_entrada in enumerate(['Aleatorio', 'Crescente', 'Decrescente']):
                dados_tipo = dados_algoritmo[dados_algoritmo['Tipo_Entrada'] == tipo_entrada]
                
                if not dados_tipo.empty:
                    # Remover valores infinitos
                    dados_tipo = dados_tipo[dados_tipo['Tempo_Medio'] < float('inf')]
                    if not dados_tipo.empty:
                        plt.plot(dados_tipo['Tamanho'], dados_tipo['Tempo_Medio'], 
                                marker='o', linewidth=2.5, markersize=6,
                                label=tipo_entrada, color=self.cores[i])
            
            plt.title(f'Desempenho do {algoritmo}', 
                     fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Tamanho do Vetor', fontweight='bold', fontsize=12)
            plt.ylabel('Tempo Medio (segundos)', fontweight='bold', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.legend(fontsize=11)
            
            plt.tight_layout()
            
            # Salvar gráfico
            nome_arquivo = f'grafico_individual_{algoritmo.replace(" ", "_").replace("(", "").replace(")", "")}.png'
            self.salvar_grafico(nome_arquivo)
    
    def gerar_graficos_comparativos(self, df):
        """Gera gráficos comparativos por tipo de entrada"""
        print("\nGerando gráficos comparativos...")
        
        tipos_entrada = ['Aleatorio', 'Crescente', 'Decrescente']
        
        for tipo in tipos_entrada:
            plt.figure(figsize=(14, 9))
            dados_tipo = df[df['Tipo_Entrada'] == tipo]
            
            algoritmos = dados_tipo['Algoritmo'].unique()
            
            for i, algoritmo in enumerate(algoritmos):
                dados_algoritmo = dados_tipo[dados_tipo['Algoritmo'] == algoritmo]
                
                # Remover valores infinitos
                dados_algoritmo = dados_algoritmo[dados_algoritmo['Tempo_Medio'] < float('inf')]
                
                if not dados_algoritmo.empty:
                    plt.plot(dados_algoritmo['Tamanho'], dados_algoritmo['Tempo_Medio'], 
                            marker='o', linewidth=2.5, markersize=6,
                            label=algoritmo, color=self.cores[i % len(self.cores)])
            
            plt.title(f'Comparacao de Todos os Algoritmos - Entrada {tipo}', 
                     fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Tamanho do Vetor', fontweight='bold', fontsize=12)
            plt.ylabel('Tempo Medio (segundos)', fontweight='bold', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
            
            plt.tight_layout()
            
            nome_arquivo = f'grafico_comparativo_{tipo.lower()}.png'
            self.salvar_grafico(nome_arquivo)
    
    def gerar_graficos_algoritmos_rapidos(self, df):
        """Gera gráficos focando nos algoritmos O(n log n)"""
        print("\nGerando gráficos dos algoritmos rapidos...")
        
        algoritmos_rapidos = ['Quick Sort (Primeiro)', 'Quick Sort (Central)', 'Heap Sort', 'Merge Sort', 'Shell Sort']
        
        tipos_entrada = ['Aleatorio', 'Crescente', 'Decrescente']
        
        for tipo in tipos_entrada:
            plt.figure(figsize=(12, 8))
            dados_tipo = df[(df['Tipo_Entrada'] == tipo) & (df['Algoritmo'].isin(algoritmos_rapidos))]
            
            for i, algoritmo in enumerate(algoritmos_rapidos):
                dados_algoritmo = dados_tipo[dados_tipo['Algoritmo'] == algoritmo]
                
                # Remover valores infinitos
                dados_algoritmo = dados_algoritmo[dados_algoritmo['Tempo_Medio'] < float('inf')]
                
                if not dados_algoritmo.empty:
                    plt.plot(dados_algoritmo['Tamanho'], dados_algoritmo['Tempo_Medio'], 
                            marker='s', linewidth=2.5, markersize=6,
                            label=algoritmo, color=self.cores[i])
            
            plt.title(f'Algoritmos O(n log n) - Entrada {tipo}', 
                     fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Tamanho do Vetor', fontweight='bold', fontsize=12)
            plt.ylabel('Tempo Medio (segundos)', fontweight='bold', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.legend(fontsize=11)
            
            plt.tight_layout()
            
            nome_arquivo = f'grafico_rapidos_{tipo.lower()}.png'
            self.salvar_grafico(nome_arquivo)
    
    def gerar_relatorio_completo(self, df):
        """Gera um relatório completo com todos os gráficos"""
        if df is None:
            print("Erro: Nao foi possivel carregar os dados.")
            return
            
        print("=" * 70)
        print("INICIANDO GERACAO DE RELATORIO COMPLETO")
        print("=" * 70)
        
        # Gerar todos os tipos de gráficos
        self.gerar_graficos_individualmente(df)
        self.gerar_graficos_comparativos(df)
        self.gerar_graficos_algoritmos_rapidos(df)
        
        # Gerar gráfico de resumo
        self.gerar_grafico_resumo(df)
        
        print("\n" + "=" * 70)
        print("RELATORIO COMPLETO GERADO COM SUCESSO!")
        print(f"Todos os gráficos salvos na pasta: '{self.pasta_graficos}'")
        print("=" * 70)
    
    def gerar_grafico_resumo(self, df):
        """Gera um gráfico de resumo com os tempos médios"""
        print("\nGerando gráfico de resumo...")
        
        # Calcular tempo médio por algoritmo (apenas valores finitos)
        df_finito = df[df['Tempo_Medio'] < float('inf')]
        tempo_medio_por_algoritmo = df_finito.groupby('Algoritmo')['Tempo_Medio'].mean()
        
        if not tempo_medio_por_algoritmo.empty:
            plt.figure(figsize=(12, 8))
            
            # Ordenar por tempo
            tempo_medio_por_algoritmo = tempo_medio_por_algoritmo.sort_values()
            
            bars = plt.barh(range(len(tempo_medio_por_algoritmo)), 
                           tempo_medio_por_algoritmo.values, 
                           color=self.cores[:len(tempo_medio_por_algoritmo)])
            
            plt.yticks(range(len(tempo_medio_por_algoritmo)), tempo_medio_por_algoritmo.index)
            plt.xlabel('Tempo Medio (segundos)', fontweight='bold', fontsize=12)
            plt.title('Resumo - Tempo Medio por Algoritmo', 
                     fontsize=16, fontweight='bold', pad=20)
            
            # Adicionar valores nas barras
            for i, bar in enumerate(bars):
                width = bar.get_width()
                plt.text(width + 0.001, bar.get_y() + bar.get_height()/2, 
                        f'{width:.3f}s', ha='left', va='center', fontsize=9)
            
            plt.grid(True, alpha=0.3, axis='x')
            plt.tight_layout()
            
            self.salvar_grafico('resumo_tempos_medios.png')

def main():
    gerador = GeradorGraficos()
    df = gerador.carregar_dados()
    if df is not None:
        gerador.gerar_relatorio_completo(df)

if __name__ == "__main__":
    main()