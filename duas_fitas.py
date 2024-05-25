class MaquinaDeTuringDuasFitas:
    def __init__(self, estados, simbolos_entrada, simbolos_fita, transicoes, estado_inicial, simbolo_branco, estados_finais):
        self.estados = estados
        self.simbolos_entrada = simbolos_entrada
        self.simbolos_fita = simbolos_fita
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.simbolo_branco = simbolo_branco
        self.estados_finais = estados_finais
        self.fita1 = []
        self.fita2 = []
        self.estado_atual = estado_inicial
        self.posicao_cabeca1 = 0
        self.posicao_cabeca2 = 0

    def inicializar_fitas(self, entrada):
        self.fita1 = list(entrada) + [self.simbolo_branco]
        self.fita2 = [self.simbolo_branco] * (len(entrada) + 1)
        self.posicao_cabeca1 = 0
        self.posicao_cabeca2 = 0
        self.estado_atual = self.estado_inicial

    def passo(self):
        simbolo_atual1 = self.fita1[self.posicao_cabeca1]
        simbolo_atual2 = self.fita2[self.posicao_cabeca2]
        if (self.estado_atual, simbolo_atual1, simbolo_atual2) in self.transicoes:
            transicoes_possiveis = self.transicoes[(self.estado_atual, simbolo_atual1, simbolo_atual2)]
            for estado_proximo, simbolo_escrever1, simbolo_escrever2, direcao1, direcao2 in transicoes_possiveis:
                nova_maquina = MaquinaDeTuringDuasFitas(
                    self.estados,
                    self.simbolos_entrada,
                    self.simbolos_fita,
                    self.transicoes,
                    estado_proximo,
                    self.simbolo_branco,
                    self.estados_finais
                )
                nova_maquina.fita1 = self.fita1[:]
                nova_maquina.fita2 = self.fita2[:]
                nova_maquina.fita1[self.posicao_cabeca1] = simbolo_escrever1
                nova_maquina.fita2[self.posicao_cabeca2] = simbolo_escrever2
                nova_maquina.posicao_cabeca1 = self.posicao_cabeca1 + (1 if direcao1 == 'D' else -1)
                nova_maquina.posicao_cabeca2 = self.posicao_cabeca2 + (1 if direcao2 == 'D' else -1)
                yield nova_maquina

    def executar(self, entrada):
        self.inicializar_fitas(entrada)
        configuracoes = [self]

        while configuracoes:
            configuracao_atual = configuracoes.pop()
            if configuracao_atual.estado_atual in self.estados_finais:
                print("Aceito: ", ''.join(configuracao_atual.fita1).strip(self.simbolo_branco))
                return True

            for proxima_configuracao in configuracao_atual.passo():
                configuracoes.append(proxima_configuracao)

        print("Rejeitado")
        return False

# Definição da Máquina de Turing com duas fitas e 12 estados
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'qf'}
simbolos_entrada = {'0', '1'}
simbolos_fita = {'0', '1', '_'}
transicoes = {
    ('q0', '0', '_'): {('q1', '0', '0', 'D', 'D'), ('q2', '0', '1', 'D', 'D')},
    ('q0', '1', '_'): {('q3', '1', '0', 'D', 'D')},
    ('q1', '0', '_'): {('q4', '0', '0', 'D', 'D')},
    ('q1', '1', '_'): {('q5', '1', '1', 'D', 'D')},
    ('q2', '0', '_'): {('q6', '0', '0', 'D', 'D')},
    ('q2', '1', '_'): {('q7', '1', '1', 'D', 'D')},
    ('q3', '0', '_'): {('q8', '0', '0', 'D', 'D')},
    ('q3', '1', '_'): {('q9', '1', '1', 'D', 'D')},
    ('q4', '0', '_'): {('q10', '0', '0', 'D', 'D')},
    ('q5', '1', '_'): {('q11', '1', '1', 'D', 'D')},
    ('q6', '0', '_'): {('qf', '0', '0', 'D', 'D')},
    ('q7', '1', '_'): {('qf', '1', '1', 'D', 'D')},
    ('q8', '0', '_'): {('qf', '0', '0', 'D', 'D')},
    ('q9', '1', '_'): {('qf', '1', '1', 'D', 'D')},
    ('q10', '0', '_'): {('qf', '0', '0', 'D', 'D')},
    ('q11', '1', '_'): {('qf', '1', '1', 'D', 'D')}
}
estado_inicial = 'q0'
simbolo_branco = '_'
estados_finais = {'qf'}

maquina = MaquinaDeTuringDuasFitas(estados, simbolos_entrada, simbolos_fita, transicoes, estado_inicial, simbolo_branco, estados_finais)

# Exemplo 1
entrada1 = "010101"
print(f"Executando a Máquina de Turing ND com duas fitas com entrada: {entrada1}")
maquina.executar(entrada1)

# Exemplo 2
entrada2 = "111000"
print(f"Executando a Máquina de Turing ND com duas fitas com entrada: {entrada2}")
maquina.executar(entrada2)

