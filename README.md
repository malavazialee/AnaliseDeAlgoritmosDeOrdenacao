Análise de Algoritmos de Ordenação
Descrição do Projeto

Este projeto implementa e analisa nove algoritmos de ordenação clássicos através de um benchmark experimental extensivo.
Desenvolvido para a disciplina de Projeto e Análise de Algoritmos, o trabalho compara o desempenho dos algoritmos em diferentes cenários — melhor caso, caso médio e pior caso — validando as complexidades assintóticas teóricas com dados práticos.

*Algoritmos Implementados*
-Bubble Sort (versão original sem melhorias)
-Bubble Sort Melhorado (com verificação de ordenação)
-Insertion Sort (inserção direta)
-Selection Sort (seleção direta)
-Shell Sort
-Heap Sort
-Merge Sort
-Quick Sort (pivô no primeiro elemento)
-Quick Sort (pivô no elemento central)

Estrutura do Projeto
IPLPAAV4/
├── Algoritmos/
├── graficos_benchmark/
├── executar_tudo.py
├── main_benchmark.py
├── gerador_graficos_completo.py
├── teste_algoritmos.py
├── analise_assintotica.md
├── DOCUMENTACAO.pdf
├── resultados_benchmark_completo.csv
├── README.md
└── .gitignore

*Requisitos do Sistema:*
-Python 3.7 ou superior

*Bibliotecas:*
-matplotlib
-pandas
-numpy

*Instalação das Dependências*
-pip install matplotlib pandas numpy

*Como Executar*
-Execução Completa (Recomendada)
-python executar_tudo.py


*Este script executa automaticamente:*
-Verificação de dependências
-Benchmark completo (~1.215 testes)
-Geração de todos os gráficos de análise
-Criação de relatórios comparativos

Execução Individual
# Validar corretude dos algoritmos
python teste_algoritmos.py

# Executar apenas o benchmark
python main_benchmark.py

# Gerar gráficos (após executar o benchmark)
python gerador_graficos_completo.py

Configurações do Benchmark
Parâmetros de Teste

*Tamanhos de vetor:*
1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000 elementos

*Tipos de entrada:*
-Aleatório (caso médio)
-Crescente (melhor caso)
-Decrescente (pior caso)

*Repetições adaptativas:*
n ≤ 5000: 5 repetições
5000 < n ≤ 20000: 3 repetições
n > 20000: 2 repetições

*Estatísticas do Benchmark*
Item	Quantidade
Total de algoritmos	9
Total de tamanhos testados	9
Total de tipos de entrada	3
Total de testes executados	≈ 1.215
Tempo estimado	15–45 minutos
Resultados e Análises
Gráficos Gerados

*O sistema gera automaticamente quatro categorias de gráficos:*
-Gráficos Individuais: desempenho de cada algoritmo nos três tipos de entrada
-Gráficos Comparativos: comparação entre todos os algoritmos por tipo de entrada
-Gráficos de Algoritmos Rápidos: foco nos algoritmos O(n log n)
-Resumo Executivo: ranking de eficiência e tempos médios



*Principais Resultados*
-Hierarquia confirmada: algoritmos O(n log n) são 20–50x mais rápidos que os O(n²) para n=20.000
-Comportamentos específicos: melhor/pior casos confirmam teoria
-Constantes ocultas: Quick Sort ≈ 2x mais rápido que Merge Sort


*Recomendações práticas:*
-Quick Sort (Central) → uso geral
-Insertion Sort → arrays pequenos

Complexidades Teóricas
| Algoritmo | Complexidade | n=10.000 (s) | Crescimento | Estável |
|-----------|--------------|--------------|-------------|---------|
| Quick Sort (Central) | O(n log n) | 0.008             | Não |
| Quick Sort (Primeiro) | O(n log n) | 0.009            | Não |
| Merge Sort | O(n log n) | 0.015                       | Sim |
| Heap Sort | O(n log n) | 0.018                        | Não |
| Shell Sort | ~O(n log n) | 0.012                      | Não |
| Insertion Sort | O(n²) | 0.180                        | Sim |
| Selection Sort | O(n²) | 0.200                        | Não |
| Bubble Sort (Melhorado) | O(n²) | 0.350               | Sim |
| Bubble Sort (Básico) | O(n²) | 0.400                  | Sim |

*Conclusões*
-Validação Científica
-Comportamentos assintóticos teóricos confirmados experimentalmente
-Hierarquia de eficiência mantida na prática
-Casos específicos comportam-se conforme esperado


*Documentação Complementar*
-analise_assintotica.md → análise teórica detalhada
-DOCUMENTACAO.pdf → documentação técnica completa
-resultados_benchmark_completo.csv → dataset completo dos resultados

*Desenvolvimento*
-Autores
-Alexandre Malavazi
-Ryan Rocha

*Instituição*
FCT/Unesp – Presidente Prudente
Disciplina: Projeto e Análise de Algoritmos – 2025
Professor: Danilo Medeiros Eler

*Metodologia*
-Implementações modulares e testáveis
-Verificação automática de correção
-Medição de alta precisão com time.perf_counter()
-Tratamento robusto de erros e exceções

*Data: Novembro de 2025*
*Versão: 1.0*
*Licença: Acadêmica*
