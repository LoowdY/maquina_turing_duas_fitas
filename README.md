# Máquinas de Turing Indeterminísticas em Python

## Introdução

Este documento descreve duas implementações de Máquinas de Turing em Python, projetadas por João Renan Lopes, Pedro Henrique Coimbra e Carlos Egger. 

## Máquina de Turing Indeterminística de Fita Única

### Descrição

Verifica se uma cadeia é um palíndromo usando 12 estados e transições aleatórias.

### Componentes e Métodos

- **Inicialização**: Define estados, alfabeto, transições, estado inicial, aceitação e rejeição.
- **Inicializar Fita**: Carrega a cadeia na fita e posiciona a cabeça de leitura/escrita.
- **Passo**: Seleciona uma transição aleatória, atualiza o estado e a posição da cabeça.
- **Executar**: Processa até atingir um estado de aceitação ou rejeição.
- **Imprimir Estado Final**: Mostra o estado final, conteúdo da fita e posição da cabeça.

## Máquina de Turing de Duas Fitas (múltiplas fitas)

### Descrição

Compara duas cadeias nas fitas para determinar se são idênticas.

### Componentes e Métodos

- **Inicialização**: Configura estados, alfabetos, transições, estado inicial, aceitação e rejeição para duas fitas.
- **Inicializar Fitas**: Carrega as cadeias e define as posições iniciais das cabeças de leitura/escrita.
- **Passo**: Realiza um passo para cada fita com base em transições aleatórias.
- **Executar**: Opera até um estado de aceitação ou rejeição ser alcançado em ambas as fitas.
- **Imprimir Estado Final**: Exibe o estado final, conteúdo das fitas e posição das cabeças.

## Dificuldades Encontradas

- **Indeterminismo**: A seleção de transições aleatórias introduziu complexidade no teste e na verificação das máquinas.
- **Sincronização de Fitas**: Para a máquina de duas fitas, garantir a sincronização adequada e a comparação precisa entre as cadeias foi desafiador.
- **Otimização de Desempenho**: Melhorar a eficiência das máquinas, especialmente com entradas maiores, exigiu ajustes significativos nas funções de transição e gerenciamento de estados.

## Conclusão

As implementações de Máquinas de Turing  demonstram a flexibilidade e a complexidade de adaptar conceitos teóricos para soluções programáticas práticas. Esses modelos são fundamentais para entender o processamento de linguagens formais e algoritmos de decisão em computação.
