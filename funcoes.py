"""O objetivo dessa classe é definir funções que recebam uma fórmula como entrada
e façam cálculos a partir de sua estrutura sintática"""

from formula import *


def tamanho(formula):
    """Determina o tamanho da fórmula em lógica proposicional"""
    if isinstance(formula, Atomica):
        return 1
    if isinstance(formula, Nao):
        return tamanho(formula.dentro) + 1
    if isinstance(formula, Implica) or isinstance(formula, E) or isinstance(formula, Ou):
        return tamanho(formula.esquerda) + tamanho(formula.direita) + 1


def subformulas(formula):
    """Retorna o X de todas as sub-fórmulas de uma fórmula.
    Por exemplo, observe o pedaço de código abaixo.
    $ minha_formula = Implica(Atomica('p'), Ou(Atomica('p'), Atomica('s')))
      for subformula in subformulas(minha_formula):
        print(subformula)
    Essa parte do código imprime: p, s, (p V s), (p → (p V s))
    (*** Note que não há repetição do p ***)
    """

    if isinstance(formula, Atomica):
        return {formula}
    if isinstance(formula, Nao):
        return {formula}.union(subformulas(formula.dentro))
    if isinstance(formula, Implica) or isinstance(formula, E) or isinstance(formula, Ou):
        sub1 = subformulas(formula.esquerda)
        sub2 = subformulas(formula.direita)
        return {formula}.union(sub1).union(sub2)

# Vimos que nessa classe, para toda fórmula A, len(subformulas(A))  <= tamanho(A).
