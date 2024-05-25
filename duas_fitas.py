#João Renan, Carlos Egger, Pedro Coimbra.
#trabalho de teoria da computabildiade e linguagens formais e automatos


# Definição da Classe MaquinaDeTuringDuasFitas com o __init__ (construtor).
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

    #inicializar variáveis e arrays (fitas da máquina de turing) para armazenar valroes das fitas, bem como o valor das cabeças da máquina.
    def inicializar_fitas(self, entrada):
        self.fita1 = list(entrada) + [self.simbolo_branco]
        self.fita2 = [self.simbolo_branco] * (len(entrada) + 1)
        self.posicao_cabeca1 = 0
        self.posicao_cabeca2 = 0
        self.estado_atual = self.estado_inicial

    
#função para relaizar transição entre estados (espécie de função de transição)
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
#executa máquinas. (iniciaçlização e invocação de função)
    def executar(self, entrada):
        self.inicializar_fitas(entrada)
        configuracoes = [self]

        while configuracoes:
            configuracao_atual = configuracoes.pop()
            if configuracao_atual.estado_atual in self.estados_finais:
                print("Aceito: ", ''.join(configuracao_atual.fita1).strip(self.simbolo_branco))
                configuracao_atual.imprimir_estado()
                return True

            for proxima_configuracao in configuracao_atual.passo():
                configuracoes.append(proxima_configuracao)

        #printa o resultado caso seja rejeitado
        print("Rejeitado")
        return False
    
#função que vai imprimir estado da mpaquina (necessário apra feedback ao usuário)
    def imprimir_estado(self):
        # Imprime o estado atual da máquina, incluindo as fitas e posições dos cabeçotes
        fita1_str = ''.join(self.fita1)
        fita2_str = ''.join(self.fita2)
        cabeçote1 = ' ' * self.posicao_cabeca1 + '^'
        cabeçote2 = ' ' * self.posicao_cabeca2 + '^'
        print(f"Estado atual: {self.estado_atual}")
        print(f"Fita 1: {fita1_str}")
        print(f"Fita 2: {fita2_str}")
        print(f"Posição cabeçote 1: {cabeçote1}")
        print(f"Posição cabeçote 2: {cabeçote2}")
        print()
        
#printa funções de tansição do automato
def print_automaton(transicoes):
    print("Autômato da Máquina de Turing:")
    for (estado_atual, simbolo_atual1, simbolo_atual2), transicoes_possiveis in transicoes.items():
        for transicao in transicoes_possiveis:
            estado_proximo, simbolo_escrever1, simbolo_escrever2, direcao1, direcao2 = transicao
            print(f"({estado_atual}, {simbolo_atual1}, {simbolo_atual2}) -> ({estado_proximo}, {simbolo_escrever1}, {simbolo_escrever2}, {direcao1}, {direcao2})")


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

# Entrada do exemplo 1 (alfabeto 0 e 1)
entrada1 = "010101"
print(f"Executando a Máquina de Turing ND com duas fitas com entrada: {entrada1}")
maquina.executar(entrada1)

# Entrada do exemplo 2 (alfabeto 0 e 1)
entrada2 = "111000"
print(f"Executando a Máquina de Turing ND com duas fitas com entrada: {entrada2}")
maquina.executar(entrada2)

# Chamada da função de impressão do autômato
print_automaton(transicoes)
