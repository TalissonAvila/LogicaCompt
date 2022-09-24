# lista 1 questão 1


from formula import *


def numeroConectivos(formula):
    if isinstance(formula, Atomica):
        return 0
    if isinstance(formula, Nao):
        return 1 + numeroConectivos(formula.dentro)
    if isinstance(formula, Implica) or isinstance(formula, E) or isinstance(formula, Ou):
        return 1 + numeroConectivos(formula.esquerda) + numeroConectivos(formula.direita)


p = Atomica('p')
q = Atomica('q')
formulaQ1 = Implica(Nao(Atomica('p')), Nao(Atomica('q')))
print(f'Número de conectivos de {formulaQ1} é igual a {numeroConectivos(formulaQ1)}')
