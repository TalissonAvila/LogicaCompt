"""Você pode testar suas funções lógicas no código abaixo: """
# Aluno Talisson Freitas Avila

from funcoes import *
from formula import *

formula1 = Atomica('p')  # p
formula2 = Atomica('q')  # q
formula3 = E(formula1, formula2)  # p ∧ q
formula4 = E(Atomica('p'), Atomica('q'))  # p ∧ q
formula5 = Nao(E(Atomica('p'), Atomica('s')))  # ¬(p ∧ s)
formula6 = Ou(Nao(E(Atomica('p'), Atomica('s'))), Atomica('q'))  # ¬(p ∧ s) V q
formula7 = Implica(Nao(E(Atomica('p'), Atomica('s'))), E(Atomica('q'), Atomica('r')))  # ¬(p ∧ s) → (q ∧ r)
formula8 = Implica(Nao(E(Atomica('p'), Atomica('s'))),
                   E(Atomica('q'), Nao(E(Atomica('q'), Atomica('s')))))  # ¬(p ∧ s) → (q ∧ ¬(q ∧ s))
formula9 = E(formula1, formula2)  # p ∧ q

if formula9 == formula3:
    print(f'{formula9} é igual a {formula3}')
else:
    print(f'{formula1} não é igual a {formula3}')

if formula1 == formula3:
    print(f'{formula1} é igual a {formula3}')
else:
    print(f'{formula1} não é igual a {formula3}')

print(formula3 == E(Atomica('p'), Atomica('q')))

print('fórmula 1:', formula1)
print('fórmula 2:', formula2)
print('fórmula 3:', formula3)
print('fórmula 4:', formula4)
print('fórmula 5:', formula5)
print('fórmula 6:', formula6)
print('fórmula 7:', formula7)
print('fórmula 8:', formula8)

print('Tamanho da fórmula 1:', tamanho(formula1))
print('Tamanho da fórmula 3:', tamanho(formula3))
print('Tamanho da fórmula 7:', tamanho(formula7))

print('sub-formulas da fórmula 7:')
# print(subformulas(formula7))
for subformula in subformulas(formula7):
    print(subformula)

print('Tamanho da fórmula 8:', tamanho(formula8))
print('sub-fórmulas of fórmula 8:')
for subformula in subformulas(formula8):
    print(subformula)

# Vimos que nessa classe, para toda fórmula A, len(subformulas(A))  <= tamanho(A).
# Por examplo, para a formula 8:
print('número de sub-fórmulas da fórmula 8:', len(subformulas(formula8)))
print('len(subformulas(formula8)) <= tamanho(formula8):', len(subformulas(formula8)) <= tamanho(formula8))
