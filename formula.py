"""Essa classe foi criada para definir fórmulas na lógica proposicional.
Por exemplo, a parte de código abaixo cria um objeto representando (p V s).
$ formula1 = Or(Atmocia('p'),Atomica('s'))
A fim de didática, o exemplo abaixo cria um objeto representando (p → (p V s).
$ formula2 = Implica(Atomica('p'),E(Atomica('p'),Atomica('s'))) 
"""


class Formula:
    def __int__(self):
        pass


class Atomica(Formula):
    """Essa parte do código representa as variáveis da lógica proposicional"""

    def __init__(self, nome):
        super().__int__()
        self.nome = nome

    def __str__(self):
        return str(self.nome)

    def __eq__(self, outro):
        return isinstance(outro, Atomica) and outro.nome == self.nome

    def __hash__(self):
        return hash((self.nome, 'atômica'))


class Implica(Formula):

    def __init__(self, esquerda, direita):
        super().__int__()
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return "(" + self.esquerda.__str__() + " " + u"\u2192" + " " + self.direita.__str__() + ")"

    def __eq__(self, outro):
        return isinstance(outro, Implica) and outro.esquerda == self.esquerda and outro.direita == self.direita

    def __hash__(self):
        return hash((hash(self.esquerda), hash(self.direita), 'implica'))


class Nao(Formula):

    def __init__(self, dentro):
        super().__int__()
        self.dentro = dentro

    def __str__(self):
        return "(" + u"\u00ac" + str(self.dentro) + ")"

    def __eq__(self, outro):
        return isinstance(outro, Nao) and outro.dentro == self.dentro

    def __hash__(self):
        return hash((hash(self.dentro), 'não'))


class E(Formula):

    def __init__(self, esquerda, direita):
        super().__init__()
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return "(" + self.esquerda.__str__() + " " + u"\u2227" + " " + self.direita.__str__() + ")"

    def __eq__(self, outro):
        return isinstance(outro, E) and outro.esquerda == self.esquerda and outro.direita == self.direita

    def __hash__(self):
        return hash((hash(self.esquerda), hash(self.direita), 'e'))


class Ou(Formula):

    def __init__(self, esquerda, direita):
        super().__init__()
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return "(" + self.esquerda.__str__() + " " + u"\u2228" + " " + self.direita.__str__() + ")"

    def __eq__(self, outro):
        return isinstance(outro, Ou) and outro.esquerda == self.esquerda and outro.direita == self.direita

    def __hash__(self):
        return hash((hash(self.esquerda), hash(self.direita), 'ou'))
