class MaquinaDeTuringND:
    def __init__(self, estados, simbolos_entrada, simbolos_fita, transicoes, estado_inicial, simbolo_branco, estados_finais):
        self.estados = estados
        self.simbolos_entrada = simbolos_entrada
        self.simbolos_fita = simbolos_fita
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.simbolo_branco = simbolo_branco
        self.estados_finais = estados_finais
        self.fita = []
        self.estado_atual = estado_inicial
        self.posicao_cabeca = 0

    def inicializar_fita(self, entrada):
        self.fita = list(entrada) + [self.simbolo_branco]
        self.posicao_cabeca = 0
        self.estado_atual = self.estado_inicial

    def passo(self):
        simbolo_atual = self.fita[self.posicao_cabeca]
        if (self.estado_atual, simbolo_atual) in self.transicoes:
            transicoes_possiveis = self.transicoes[(self.estado_atual, simbolo_atual)]
            for estado_proximo, simbolo_escrever, direcao in transicoes_possiveis:
                nova_maquina = MaquinaDeTuringND(
                    self.estados,
                    self.simbolos_entrada,
                    self.simbolos_fita,
                    self.transicoes,
                    estado_proximo,
                    self.simbolo_branco,
                    self.estados_finais
                )
                nova_maquina.fita = self.fita[:]
                nova_maquina.fita[self.posicao_cabeca] = simbolo_escrever
                nova_maquina.posicao_cabeca = self.posicao_cabeca + (1 if direcao == 'D' else -1)
                yield nova_maquina

    def executar(self, entrada):
        self.inicializar_fita(entrada)
        configuracoes = [self]

        while configuracoes:
            configuracao_atual = configuracoes.pop()
            if configuracao_atual.estado_atual in self.estados_finais:
                print("Aceito: ", ''.join(configuracao_atual.fita).strip(self.simbolo_branco))
                return True

            for proxima_configuracao in configuracao_atual.passo():
                configuracoes.append(proxima_configuracao)

        print("Rejeitado")
        return False

# Definição da Máquina de Turing Não Determinística com 12 estados
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'qf'}
simbolos_entrada = {'0', '1'}
simbolos_fita = {'0', '1', '_'}
transicoes = {
    ('q0', '0'): {('q1', '0', 'D'), ('q2', '1', 'D')},
    ('q0', '1'): {('q3', '1', 'D')},
    ('q1', '0'): {('q4', '0', 'D')},
    ('q1', '1'): {('q5', '1', 'D')},
    ('q2', '0'): {('q6', '0', 'D')},
    ('q2', '1'): {('q7', '1', 'D')},
    ('q3', '0'): {('q8', '0', 'D')},
    ('q3', '1'): {('q9', '1', 'D')},
    ('q4', '0'): {('q10', '0', 'D')},
    ('q5', '1'): {('q11', '1', 'D')},
    ('q6', '0'): {('qf', '0', 'D')},
    ('q7', '1'): {('qf', '1', 'D')},
    ('q8', '0'): {('qf', '0', 'D')},
    ('q9', '1'): {('qf', '1', 'D')},
    ('q10', '0'): {('qf', '0', 'D')},
    ('q11', '1'): {('qf', '1', 'D')}
}
estado_inicial = 'q0'
simbolo_branco = '_'
estados_finais = {'qf'}

maquina = MaquinaDeTuringND(estados, simbolos_entrada, simbolos_fita, transicoes, estado_inicial, simbolo_branco, estados_finais)

# Exemplo 1
entrada1 = "010101"
print(f"Executando a Máquina de Turing ND com entrada: {entrada1}")
maquina.executar(entrada1)

# Exemplo 2
entrada2 = "111000"
print(f"Executando a Máquina de Turing ND com entrada: {entrada2}")
maquina.executar(entrada2)
