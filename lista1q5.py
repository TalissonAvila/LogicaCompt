# lista 1 questão 5 / Forma reduzida

from funcoes import *


def atomicas(formula):
    if isinstance(formula, Atomica):
        lista_de_atomicas = [formula.nome]
        return set(lista_de_atomicas)
    if isinstance(formula, Nao):
        return atomicas(formula.dentro)
    if isinstance(formula, Implica) or isinstance(formula, E) or isinstance(formula, Ou):
        return atomicas(formula.esquerda) | atomicas(formula.direita)


p = Atomica('p')
q = Atomica('q')
s = Atomica('s')
formula1Q5 = Ou(E(p, Nao(Implica(p, Nao(q)))), Nao(q))
formula2Q5 = Ou(Nao(E(p, s)), p)
print(f'A fórmula {formula1Q5} tem como atômicas {atomicas(formula1Q5)}')
print(f'A fórmula {formula2Q5} tem como atômicas {atomicas(formula2Q5)}')

teste1 = Atomica('x+1')
teste2 = Atomica('x-3')
x = Atomica('x')
formulateste = Ou(teste1, Implica(x, teste2))
print(f'A fórmula {formulateste} tem como atômicas {atomicas(formulateste)}')
