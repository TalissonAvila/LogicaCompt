# lista 1 questão 5

from funcoes import *


def atomicas(formula):
    if isinstance(formula, Atomica):
        return formula.nome
    if isinstance(formula, Nao):
        return atomicas(formula.dentro)
    if isinstance(formula, Implica) or isinstance(formula, E) or isinstance(formula, Ou):
        return atomicas(formula.esquerda) + atomicas(formula.direita)


p = Atomica('p')
q = Atomica('q')
s = Atomica('s')
formula1Q5 = Ou(E(p, Nao(Implica(p, Nao(q)))), Nao(q))
formula2Q5 = Ou(Nao(E(p, s)), p)
print(f'A fórmula {formula1Q5} tem como atômicas {set(atomicas(formula1Q5))}')
print(f'A fórmula {formula2Q5} tem como atômicas {set(atomicas(formula2Q5))}')
