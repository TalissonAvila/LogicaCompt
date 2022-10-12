from atoms import *
from math import sqrt
from time import time
from semanticas import satisfabilidade_forca_bruta
'''
No sudoku 4x4 é preciso preencher os quadrados de um grid de 4 linhas e 4 colunas com números de 1 a 4, 
e eles não podem se repetir na mesma linha, coluna ou subgrid.
'''

sudoku1 = [[0, 1, 4, 3],
           [4, 3, 2, 0],
           [1, 0, 3, 4],
           [3, 4, 1, 0]]

sudoku2 = [[0, 4, 3, 2],
           [0, 0, 1, 4],
           [2, 3, 0, 1],
           [4, 1, 2, 0]]

"""
sudoku1_solucao = [[2, 1, 4, 3],
                    [4, 3, 2, 1],
                    [1, 2, 3, 4],
                    [3, 4, 1, 2]]
"""


# atomica 1_1_1 diz que na célula (1,1) está preenchida com 1
# atomica 2_3_4 diz que na célula (2,3) está preenchica com 4

# a sulução do sudoku precisa concordar com os números preenchidos previamente

def restricao_numero_dados(grid):
    """
    Retorna uma formula que força o valor verdade das atomicas atraves dos numeros previamente preenchidos no
    grid sukodu.
    :param grid: um grid sudoku
    :return: formula E
    """
    formula_dadas = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                formula_dadas.append(Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(grid[i][j])))
                for n in range(1, len(grid) + 1):
                    if n != grid[i][j]:
                        formula_dadas.append(Nao(Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(n))))
    return e_de_todos(formula_dadas)


def e_de_todos(lista_de_formulas):
    """
    Retorna uma formula 'Ezao' de uma lista de formulas
    :param lista_de_formulas: uma lista de formuals
    :return: formula E
    """
    primeira_formula = lista_de_formulas[0]
    del lista_de_formulas[0]
    for formula in lista_de_formulas:
        primeira_formula = E(primeira_formula, formula)
    return primeira_formula


def ou_de_todos(lista_de_formulas):
    """
    Retrona uma formula 'Ouzao' de uma lista de formulas.
    :param lista_de_formulas: uma lsita de formulas
    :return: formula Ou
    """
    primeira_formula = lista_de_formulas[0]
    del lista_de_formulas[0]
    for formula in lista_de_formulas:
        primeira_formula = Ou(primeira_formula, formula)
    return primeira_formula


def restricao_linha(grid):
    """
    Retrona uma formula impondo que cada linha tem de ser preenchida com todos os numeros (1 a 4).
    :param grid: um grid sukodu
    :return: formula E
    """
    formula_linha = []
    for i in range(len(grid)):
        for n in range(len(grid)):
            lista_de_ou = []
            for j in range(len(grid)):
                lista_de_ou.append(Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)))
            formula_ou = ou_de_todos(lista_de_ou)
            formula_linha.append(formula_ou)
    return e_de_todos(formula_linha)


def restricao_celulas(grid):
    """
    Retorna uma formula que requer que cada celula não pode ser preenchida com mais de um numero.
    :param grid: grid sudoku
    :return: formula E
    """
    formula_celulas = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            for n1 in range(len(grid) - 1):
                for n2 in range(n1 + 1, len(grid)):
                    formula_celulas.append(Nao(E(Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(n1 + 1)),
                                                 Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(n2 + 1)))))
    return e_de_todos(formula_celulas)


def restricao_colunas(grid):
    """
    Retrona uma formula impondo que cada coluna deve ser preenchida com todos os numeros (1 a 4).
    :param grid: um grid sudoku
    :return: formula E
    """
    formula_colunas = []
    for j in range(len(grid)):
        for n in range(len(grid)):
            lista_de_ou = []
            for i in range(len(grid)):
                lista_de_ou.append(Atomica(str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)))
            formula_ou = ou_de_todos(lista_de_ou)
            formula_colunas.append(formula_ou)
    return e_de_todos(formula_colunas)


def restricao_subgrid(grid):
    """
    Retorna uma formula impondo que cada subgrid deve ser preenchido com todos os numeros (1 a 4).
    :param grid: um grod sudoku
    :return: formula E
    """
    formula_subgrids = []
    for sl in range(int(sqrt(len(grid)))):
        for sc in range(int(sqrt(len(grid)))):
            for n in range(len(grid)):
                lista_de_ou = []
                for i in range(2):
                    for j in range(2):
                        lista_de_ou.append(Atomica(str(sl * 2 + i + 1) + '_' + str(sc * 2 + j + 1) + '_' + str(n + 1)))
                formula_ou = ou_de_todos(lista_de_ou)
                formula_subgrids.append(formula_ou)
    return e_de_todos(formula_subgrids)


def solucao_sudoku(grid):
    """

    :param grid: um grid sudoku
    """
    final_formula = E(
        E(
            E(
                restricao_numero_dados(grid),
                restricao_linha(grid)
            ),
            E(
                restricao_celulas(grid),
                restricao_colunas(grid)
            ),
        ),
        restricao_subgrid(sudoku1)
    )
    solucao = satisfabilidade_forca_bruta(final_formula)
    if solucao:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    for n in range(len(grid)):
                        if solucao[str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)]:
                            grid[i][j] = n + 1
                            break
        print(grid)
    else:
        print('Sudoku sem solução.')


tempo_inicio = time()
# print('Solução do sudoku: ')
# solucao_sudoku(sudoku1)
tempo_final = time()
tempo_total = tempo_final - tempo_inicio
print(f'Tempo total para resolver o sudoku foi de : {tempo_total}')
