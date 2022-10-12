from formula import *
from atoms import *


def valor_verdade(formula, interpretacao: dict):
    if isinstance(formula, Atomica):
        lista_atomicas = atomicas(formula)
        for atomica in lista_atomicas:
            if interpretacao[str(atomica.nome)] == True:
                return True
            elif interpretacao[str(atomica.nome)] == False:
                return False
            else:
                return "A interpretação de uma atômica pode receber valores somente de True ou False."

    if isinstance(formula, Nao):
        valoracao = valor_verdade(formula.dentro, interpretacao)
        if valoracao == True:
            return False
        elif valoracao == False:
            return True
        else:
            return "A interpretação de uma atômica pode receber valores somente de True ou False."

    if isinstance(formula, E):
        formula_esquerda = valor_verdade(formula.esquerda, interpretacao)
        formula_direita = valor_verdade(formula.direita, interpretacao)

        if type(formula_esquerda) != bool or type(formula_direita) != bool:
            return "A interpretação de uma atômica pode receber valores somente de True ou False."
        if formula_esquerda and formula_direita:
            return True
        else:
            return False

    if isinstance(formula, Ou):
        formula_esquerda = valor_verdade(formula.esquerda, interpretacao)
        formula_direita = valor_verdade(formula.direita, interpretacao)

        if type(formula_esquerda) != bool or type(formula_direita) != bool:
            return "A interpretação de uma atômica pode receber valores somente de True ou False."
        if formula_esquerda == False and formula_direita == False:
            return False
        else:
            return True


def sat(formula, lista_atomicas, interpretacao: dict):
    if not atomicas():
        hipotese_valoracao = valor_verdade(formula, interpretacao)
        if hipotese_valoracao:
            return interpretacao
        else:
            return False

    lista_atomicas = atomicas().copy()
    nova_lista = interpretacao.copy()
    atomica = lista_atomicas.pop()
    # interpretacao1 = dict(nova_lista, **{str(atomica.nome): True})
    # interpretacao2 = dict(nova_lista, **{str(atomica.nome): False})
    interpretacao1 = interpretacao | {atomica.nome: True}
    interpretacao2 = interpretacao | {atomica.nome: False}
    resultado = sat(formula, lista_atomicas, interpretacao1)
    if resultado != False:
        return resultado
    return sat(formula, lista_atomicas, interpretacao2)


def satisfabilidade_forca_bruta(formula: Formula, interpretacao_antes: dict = {}):
    """
    Checa se um formula é satisfativel. Em outras palavras, se a formula de entrada é
    satisfativel, ela retornará uma interpretação que atribui 'True' à formula.
    Caso contrario, ela retornará 'False'.
    """
    pass
    lista_atomicas = list(atomicas(formula))
    interpretacao = interpretacao_antes.copy()
    interpretacao_inicial_atomicas = list(interpretacao.keys())
    for atomica in lista_atomicas:
        if atomica.nome in interpretacao_inicial_atomicas:
            lista_atomicas.remove(atomica)
    return sat(formula, lista_atomicas, interpretacao)
