# Máquina de Turing Não Determinística em Python

## Descrição

Este projeto implementa uma Máquina de Turing Não Determinística (MTND) em Python, com interação do usuário. A Máquina de Turing é um modelo computacional teórico que consiste em uma fita infinita que pode ser lida e escrita, um cabeçote de leitura/escrita que se move pela fita e uma tabela de transições que define as regras para mover o cabeçote e modificar a fita. É usada para formalizar o conceito de computação e para estudar os limites do que pode ser computado.

## O que é uma Máquina de Turing Não Determinística?

Uma Máquina de Turing Não Determinística (MTND) é uma variação da Máquina de Turing clássica. Em vez de ter apenas uma transição possível para cada combinação de estado e símbolo na fita, pode haver várias transições possíveis. Isso significa que a MTND pode "escolher" entre vários caminhos possíveis de execução, permitindo que explore várias computações em paralelo.

## Estrutura do Código

### Classe `MaquinaDeTuringND`

A classe encapsula os estados, símbolos de entrada e fita, transições, estado inicial, símbolo branco, estados finais e a lógica para inicializar a fita, realizar um passo de computação e executar a máquina.

- **`__init__`**: Inicializa a máquina com estados, símbolos, transições, estado inicial, símbolo branco e estados finais.
- **`inicializar_fita`**: Configura a fita inicial com a entrada fornecida.
- **`passo`**: Realiza um passo de computação, gerando novas máquinas de Turing com as possíveis transições.
- **`executar`**: Executa a máquina de Turing, explorando todas as configurações possíveis até encontrar uma que leva a um estado final ou esgotar as possibilidades.

##Desenvolvedores:  
-João Renan Santanna Lopes
-Pedro Henrique Costa Coimbra
-Carlos Egger Carvalho Miranda
