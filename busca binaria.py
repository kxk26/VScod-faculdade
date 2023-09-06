

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio =(minimo + maximo // 2)
        # Verifica se o valor procurado esta a esquerda ou a direita do valor central
        if valor < lista [meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui 
    return False #se chegar até aqui, significa que o valor não foi encontrado      