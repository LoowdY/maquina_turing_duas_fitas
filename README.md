# Máquinas de Turing Indeterminísticas em Python

## Introdução

Este documento descreve duas implementações de Máquinas de Turing em Python. A primeira é uma Máquina de Turing indeterminística de fita única, enquanto a segunda é uma Máquina de Turing indeterminística de duas fitas. Cada uma dessas máquinas é capaz de processar cadeias de entrada e determinar se elas satisfazem certas condições especificadas pelas funções de transição. Este trabalho foi desenvolvido por João Renan Lopes, Pedro Coimbra e Carlos Egger.

## Máquina de Turing Indeterminística de Fita Única

### Descrição

A primeira implementação é uma Máquina de Turing indeterminística que verifica se uma cadeia é um palíndromo. Ela possui 12 estados e usa transições aleatórias para determinar o próximo estado e operação. A máquina imprime o estado final e o conteúdo da fita ao terminar.

### Explicação

- **Inicialização**: A máquina é inicializada com os estados, alfabetos, função de transição, estado inicial, estado de aceitação e estado de rejeição.
- **Inicializar Fita**: Este método inicializa a fita com a cadeia de entrada e define a posição inicial da cabeça de leitura/escrita.
- **Passo**: Executa um único passo da máquina, selecionando uma transição aleatória entre as possíveis e atualizando o estado, a fita e a posição da cabeça.
- **Executar**: Este método executa a máquina até que ela alcance um estado de aceitação ou rejeição, retornando `True` se a cadeia for aceita e `False` caso contrário.
- **Imprimir Estado Final**: Método que imprime o estado final da máquina, incluindo o conteúdo da fita e a posição final da cabeça.

## Máquina de Turing Indeterminística de Duas Fitas

### Descrição

A segunda implementação é uma Máquina de Turing indeterminística de duas fitas que verifica se duas cadeias são iguais. Esta máquina compara as entradas nas duas fitas, caracter por caracter, e determina se elas são idênticas. Ela tem estados separados para processar cada fita e pode aceitar ou rejeitar baseado na igualdade das cadeias.

### Explicação

- **Inicialização**: A máquina é inicializada com os estados, alfabetos, funções de transição para cada fita, estado inicial, e estados de aceitação e rejeição.
- **Inicializar Fitas**: Este método inicializa as fitas com as cadeias de entrada e define as posições iniciais das cabeças de leitura/escrita.
- **Passo**: Executa um único passo da máquina, selecionando uma transição aleatória entre as possíveis para cada fita e atualizando os estados, as fitas e as posições das cabeças.
- **Executar**: Este método executa a máquina até que ela alcance um estado de aceitação ou rejeição em ambas as fitas, retornando `True` se as cadeias forem iguais e `False` caso contrário.
- **Imprimir Estado Final**: Método que imprime o estado final da máquina, incluindo o conteúdo das fitas e as posições finais das cabeças.
