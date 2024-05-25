#João Renan Lopes, Carlos Egger, pedro Coimbra
#Trabalho de Teoria da Computabildiade e linguagens Formais e Autômatos
#import de modluls necessarios
from collections import defaultdict
import random


#definindo classe MaquinaDeTuringIndeterministica junto com o método __init__(construtor)
class MaquinaDeTuringIndeterministica:
    def __init__(self, estados, alfabeto, alfabeto_fita, funcao_transicao, estado_inicial, estado_aceitacao, estado_rejeicao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.alfabeto_fita = alfabeto_fita
        self.funcao_transicao = defaultdict(list)
        for chave, valores in funcao_transicao.items():
            for valor in valores:
                self.funcao_transicao[chave].append(valor)
        self.estado_inicial = estado_inicial
        self.estado_aceitacao = estado_aceitacao
        self.estado_rejeicao = estado_rejeicao
        self.fita = []
        self.cabeca = 0
        self.estado_atual = estado_inicial
        
#função pra inicializar fita
    def inicializar_fita(self, cadeia_entrada):
        self.fita = list(cadeia_entrada) + ['_']
        self.cabeca = 0
        self.estado_atual = self.estado_inicial
#função pra relaizar passo (simialr a uma função de transição)
    def passo(self):
        if self.estado_atual in [self.estado_aceitacao, self.estado_rejeicao]:
            return

        simbolo_atual = self.fita[self.cabeca]
        chave = (self.estado_atual, simbolo_atual)

        if chave in self.funcao_transicao:
            transicoes_possiveis = self.funcao_transicao[chave]
            transicao_escolhida = random.choice(transicoes_possiveis)
            novo_estado, novo_simbolo, movimento = transicao_escolhida
            self.fita[self.cabeca] = novo_simbolo
            self.estado_atual = novo_estado

            self.cabeca += 1 if movimento == 'D' else -1

            if self.cabeca < 0:
                self.cabeca = 0
                self.fita.insert(0, '_')
            elif self.cabeca >= len(self.fita):
                self.fita.append('_')

    #função para executar automato (inicialziação e passo)
    def executar(self, cadeia_entrada):
        self.inicializar_fita(cadeia_entrada)
        while self.estado_atual not in [self.estado_aceitacao, self.estado_rejeicao]:
            self.passo()
        return self.estado_atual == self.estado_aceitacao
        
#função de retorno ao rusuario (retorno do estdo final q_aceito, etc..)
    def imprimir_estado_final(self):
        print("Estado final:", self.estado_atual)
        print("Conteúdo da fita:", ''.join(self.fita))
        print("Posição da cabeça:", self.cabeca)

#imprimir funções de transição do automato para melhor visiualização
def imprimir_automato(funcao_transicao):
    print("Autômato da Máquina de Turing Indeterminística:")
    for (estado_atual, simbolo_atual), transicoes in funcao_transicao.items():
        for (estado_proximo, simbolo_escrever, direcao) in transicoes:
            print(f"De ({estado_atual}, '{simbolo_atual}') para ({estado_proximo}, '{simbolo_escrever}', '{direcao}')")        

# Exemplo: Máquina de Turing Indeterminística para Verificar Palíndromos
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q_aceitar', 'q_rejeitar'}
alfabeto = {'a', 'b', 'c'}
alfabeto_fita = {'a', 'b', 'c', '_'}
funcao_transicao = {
    ('q0', 'a'): [('q1', '_', 'D'), ('q2', '_', 'D')],
    ('q0', 'b'): [('q3', '_', 'D'), ('q4', '_', 'D')],
    ('q0', 'c'): [('q5', '_', 'D'), ('q6', '_', 'D')],
    ('q0', '_'): [('q_aceitar', '_', 'N')],

    ('q1', 'a'): [('q1', 'a', 'D')],
    ('q1', 'b'): [('q1', 'b', 'D')],
    ('q1', 'c'): [('q1', 'c', 'D')],
    ('q1', '_'): [('q7', '_', 'E')],

    ('q2', 'a'): [('q2', 'a', 'D')],
    ('q2', 'b'): [('q2', 'b', 'D')],
    ('q2', 'c'): [('q2', 'c', 'D')],
    ('q2', '_'): [('q8', '_', 'E')],

    ('q3', 'a'): [('q3', 'a', 'D')],
    ('q3', 'b'): [('q3', 'b', 'D')],
    ('q3', 'c'): [('q3', 'c', 'D')],
    ('q3', '_'): [('q9', '_', 'E')],

    ('q4', 'a'): [('q4', 'a', 'D')],
    ('q4', 'b'): [('q4', 'b', 'D')],
    ('q4', 'c'): [('q4', 'c', 'D')],
    ('q4', '_'): [('q10', '_', 'E')],

    ('q5', 'a'): [('q5', 'a', 'D')],
    ('q5', 'b'): [('q5', 'b', 'D')],
    ('q5', 'c'): [('q5', 'c', 'D')],
    ('q5', '_'): [('q11', '_', 'E')],

    ('q6', 'a'): [('q6', 'a', 'D')],
    ('q6', 'b'): [('q6', 'b', 'D')],
    ('q6', 'c'): [('q6', 'c', 'D')],
    ('q6', '_'): [('q_aceitar', '_', 'N')],

    ('q7', 'a'): [('q0', '_', 'D')],
    ('q8', 'b'): [('q0', '_', 'D')],
    ('q9', 'c'): [('q0', '_', 'D')],
    ('q10', 'b'): [('q0', '_', 'D')],
    ('q11', 'c'): [('q0', '_', 'D')],
}
#definindo estado inicial e variaveis importantes de referencia para o programa
estado_inicial = 'q0'
estado_aceitacao = 'q_aceitar'
estado_rejeicao = 'q_rejeitar'


#execução principal (instacnia de objeto da classe MaquinaDeTuringIndeterministica)
mt = MaquinaDeTuringIndeterministica(estados, alfabeto, alfabeto_fita, funcao_transicao, estado_inicial, estado_aceitacao, estado_rejeicao)

cadeia_entrada = "abccba"
resultado = mt.executar(cadeia_entrada)

#controle de fluxo para verificar se foi aceita ou nao
if resultado:
    print("A cadeia foi aceita.")
else:
    print("A cadeia foi rejeitada.")

# Exemplo de uso da função para imprimir o autômato
imprimir_automato(mt.funcao_transicao)



mt.imprimir_estado_final()
