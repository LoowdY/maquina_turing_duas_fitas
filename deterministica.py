class MaquinaDeTuringDuasFitas:
    def __init__(self, estados, alfabeto, alfabeto_fita, funcao_transicao, estado_inicial, estado_aceitacao, estado_rejeicao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.alfabeto_fita = alfabeto_fita
        self.funcao_transicao = funcao_transicao
        self.estado_inicial = estado_inicial
        self.estado_aceitacao = estado_aceitacao
        self.estado_rejeicao = estado_rejeicao
        self.fita1 = []
        self.fita2 = []
        self.cabeca1 = 0
        self.cabeca2 = 0
        self.estado_atual = estado_inicial

    def inicializar_fitas(self, cadeia_entrada):
        self.fita1 = list(cadeia_entrada) + ['_']
        self.fita2 = ['_'] * len(self.fita1)
        self.cabeca1 = 0
        self.cabeca2 = 0
        self.estado_atual = self.estado_inicial

    def passo(self):
        if self.estado_atual in [self.estado_aceitacao, self.estado_rejeicao]:
            return

        simbolo_fita1 = self.fita1[self.cabeca1]
        simbolo_fita2 = self.fita2[self.cabeca2]
        chave = (self.estado_atual, simbolo_fita1, simbolo_fita2)

        if chave in self.funcao_transicao:
            novo_estado, novo_simbolo_fita1, novo_simbolo_fita2, movimento1, movimento2 = self.funcao_transicao[chave]
            self.fita1[self.cabeca1] = novo_simbolo_fita1
            self.fita2[self.cabeca2] = novo_simbolo_fita2
            self.estado_atual = novo_estado

            self.cabeca1 += 1 if movimento1 == 'D' else -1
            self.cabeca2 += 1 if movimento2 == 'D' else -1

            if self.cabeca1 < 0:
                self.cabeca1 = 0
                self.fita1.insert(0, '_')
            elif self.cabeca1 >= len(self.fita1):
                self.fita1.append('_')

            if self.cabeca2 < 0:
                self.cabeca2 = 0
                self.fita2.insert(0, '_')
            elif self.cabeca2 >= len(self.fita2):
                self.fita2.append('_')

    def executar(self, cadeia_entrada):
        self.inicializar_fitas(cadeia_entrada)
        while self.estado_atual not in [self.estado_aceitacao, self.estado_rejeicao]:
            self.passo()
        return self.estado_atual == self.estado_aceitacao

# Exemplo 1: "Duplicador"
estados = {'q0', 'q1', 'q2', 'q_aceitar', 'q_rejeitar'}
alfabeto = {'a', 'b', 'c'}
alfabeto_fita = {'a', 'b', 'c', '_'}
funcao_transicao = {
    ('q0', 'a', '_'): ('q1', 'a', 'a', 'D', 'D'),
    ('q0', 'b', '_'): ('q1', 'b', 'b', 'D', 'D'),
    ('q0', 'c', '_'): ('q1', 'c', 'c', 'D', 'D'),
    ('q0', '_', '_'): ('q2', '_', '_', 'E', 'D'),
    ('q1', 'a', '_'): ('q1', 'a', 'a', 'D', 'D'),
    ('q1', 'b', '_'): ('q1', 'b', 'b', 'D', 'D'),
    ('q1', 'c', '_'): ('q1', 'c', 'c', 'D', 'D'),
    ('q1', '_', '_'): ('q2', '_', '_', 'E', 'D'),
    ('q2', '_', 'a'): ('q2', '_', 'a', 'E', 'D'),
    ('q2', '_', 'b'): ('q2', '_', 'b', 'E', 'D'),
    ('q2', '_', 'c'): ('q2', '_', 'c', 'E', 'D'),
    ('q2', '_', '_'): ('q_aceitar', '_', '_', 'E', 'E'),
}
estado_inicial = 'q0'
estado_aceitacao = 'q_aceitar'
estado_rejeicao = 'q_rejeitar'

mt = MaquinaDeTuringDuasFitas(estados, alfabeto, alfabeto_fita, funcao_transicao, estado_inicial, estado_aceitacao, estado_rejeicao)
cadeia_entrada = "abc"
resultado = mt.executar(cadeia_entrada)
print("Resultado do Exemplo 1 (Duplicador):", resultado)

# Exemplo 2: "Palíndromo"
estados = {'q0', 'q1', 'q2', 'q3', 'q_aceitar', 'q_rejeitar'}
alfabeto = {'a', 'b', 'c'}
alfabeto_fita = {'a', 'b', 'c', '_'}
funcao_transicao = {
    ('q0', 'a', '_'): ('q1', '_', 'a', 'D', 'E'),
    ('q0', 'b', '_'): ('q1', '_', 'b', 'D', 'E'),
    ('q0', 'c', '_'): ('q1', '_', 'c', 'D', 'E'),
    ('q0', '_', '_'): ('q_aceitar', '_', '_', 'N', 'N'),
    ('q1', 'a', '_'): ('q1', 'a', '_', 'D', 'E'),
    ('q1', 'b', '_'): ('q1', 'b', '_', 'D', 'E'),
    ('q1', 'c', '_'): ('q1', 'c', '_', 'D', 'E'),
    ('q1', '_', '_'): ('q2', '_', '_', 'E', 'E'),
    ('q2', 'a', 'a'): ('q2', '_', '_', 'E', 'E'),
    ('q2', 'b', 'b'): ('q2', '_', '_', 'E', 'E'),
    ('q2', 'c', 'c'): ('q2', '_', '_', 'E', 'E'),
    ('q2', '_', '_'): ('q3', '_', '_', 'N', 'N'),
    ('q3', 'a', '_'): ('q3', '_', 'a', 'E', 'D'),
    ('q3', 'b', '_'): ('q3', '_', 'b', 'E', 'D'),
    ('q3', 'c', '_'): ('q3', '_', 'c', 'E', 'D'),
    ('q3', '_', '_'): ('q_aceitar', '_', '_', 'N', 'N'),
}
estado_inicial = 'q0'
estado_aceitacao = 'q_aceitar'
estado_rejeicao = 'q_rejeitar'

mt_palindromo = MaquinaDeTuringDuasFitas(estados, alfabeto, alfabeto_fita, funcao_transicao, estado_inicial, estado_aceitacao, estado_rejeicao)
cadeia_entrada_palindromo = "abcba"
resultado_palindromo = mt_palindromo.executar(cadeia_entrada_palindromo)
print("Resultado do Exemplo 2 (Palíndromo):", resultado_palindromo)
