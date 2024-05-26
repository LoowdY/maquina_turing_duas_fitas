# Máquinas de Turing em Python

## Introdução

Este documento descreve duas implementações de Máquinas de Turing em Python, projetadas por João Renan Lopes, Pedro Henrique Coimbra e Carlos Egger, João Severino e Rodrigo Franco. 

## Máquina de Turing Indeterminística de Fita Única

### Descrição

Verifica se uma cadeia é um palíndromo usando 12 estados e transições aleatórias.

### Componentes e Métodos

- **Inicialização**: Define estados, alfabeto, transições, estado inicial, aceitação e rejeição.
- **Inicializar Fita**: Carrega a cadeia na fita e posiciona a cabeça de leitura/escrita.
- **Passo**: Seleciona uma transição aleatória, atualiza o estado e a posição da cabeça.
- **Executar**: Processa até atingir um estado de aceitação ou rejeição.
- **Imprimir Estado Final**: Mostra o estado final, conteúdo da fita e posição da cabeça.

# Máquina de Turing com Duas Fitas - Implementação e Funcionamento

Abaixo está um detalhamento da implementação e do funcionamento de uma Máquina de Turing não-determinística com duas fitas, simulada em Python.

## Classe `MaquinaDeTuringDuasFitas`

Esta classe representa uma máquina de Turing que opera com duas fitas. Suas principais características e métodos incluem:

### Atributos
- `estados`: Conjunto de todos os estados possíveis.
- `simbolos_entrada`: Símbolos que a máquina pode receber como entrada.
- `simbolos_fita`: Símbolos que podem ser escritos nas fitas.
- `transicoes`: Dicionário mapeando a combinação de estado e símbolos lidos das duas fitas para um conjunto de possíveis ações.
- `estado_inicial`: Estado inicial da máquina.
- `simbolo_branco`: Símbolo usado para representar espaços vazios na fita.
- `estados_finais`: Conjunto de estados nos quais a máquina pode terminar sua execução.

### Métodos
- **`__init__`**: Inicializa a máquina com os parâmetros especificados.
- **`inicializar_fitas`**: Prepara as fitas com a entrada fornecida e preenche o restante com o símbolo branco.
- **`passo`**: Realiza um passo de computação baseado no estado atual e nos símbolos sob as cabeças de leitura/gravação.
- **`executar`**: Executa a máquina a partir de uma entrada, processando até alcançar um estado final ou não ter transições possíveis.
- **`imprimir_estado`**: Mostra o estado atual da máquina, incluindo o conteúdo das fitas e a posição das cabeças de leitura/gravação.

## Definição e Execução

- **Estados**: Define os estados possíveis, incluindo o estado final.
- **Símbolos de Entrada e Fita**: Define quais símbolos podem ser lidos e escritos.
- **Transições**: Mapeia os estados e símbolos lidos para possíveis novos estados e ações.
- **Inicialização e Execução**: Cria uma instância da máquina e executa com entradas de exemplo.


# Máquina de Turing Indeterminística para Verificação de Palíndromos

Este código define e simula uma Máquina de Turing Indeterminística (MTI) em Python. O propósito é verificar se uma cadeia de entrada é um palíndromo. Abaixo, está uma descrição detalhada dos componentes do código e sua funcionalidade.

## Classe `MaquinaDeTuringIndeterministica`

A classe `MaquinaDeTuringIndeterministica` simula o comportamento de uma Máquina de Turing com múltiplas possíveis transições para cada par de estado e símbolo de entrada.

### Atributos

- `estados`: Conjunto de todos os estados possíveis na máquina.
- `alfabeto`: Conjunto de símbolos que podem ser lidos na entrada.
- `alfabeto_fita`: Conjunto de símbolos que podem existir na fita.
- `funcao_transicao`: Dicionário que mapeia cada par (estado, símbolo) para uma lista de tuplas (novo_estado, símbolo a escrever, movimento da cabeça).
- `estado_inicial`: Estado inicial da máquina.
- `estado_aceitacao`: Estado que indica a aceitação da cadeia.
- `estado_rejeicao`: Estado que indica a rejeição da cadeia.
- `fita`: Lista que simula a fita da máquina de Turing.
- `cabeca`: Índice que aponta para a posição atual da cabeça de leitura/escrita na fita.
- `estado_atual`: Estado atual da máquina durante a execução.

### Métodos

- `__init__`: Construtor que inicializa a máquina com os estados, alfabeto, funções de transição e estados de aceitação/rejeição.
- `inicializar_fita`: Prepara a fita com a entrada fornecida e um símbolo de espaço ('_') no final.
- `passo`: Executa um passo da computação, onde lê o símbolo sob a cabeça de leitura, escolhe uma transição possível de forma aleatória e realiza a ação correspondente.
- `executar`: Executa a máquina até que chegue a um estado de aceitação ou rejeição.
-

## Conclusão

As implementações de Máquinas de Turing  demonstram a flexibilidade e a complexidade de adaptar conceitos teóricos para soluções programáticas práticas. Esses modelos são fundamentais para entender o processamento de linguagens formais e algoritmos de decisão em computação.
