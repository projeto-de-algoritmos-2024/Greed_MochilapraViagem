def knapsack(peso_maximo, itens):

    itens_ordenados = sorted(itens, key=lambda item: item[2] / item[1], reverse=True)

    peso_atual = 0
    valor_total = 0
    itens_escolhidos = []

    for nome, peso, valor in itens_ordenados:
        if peso_atual + peso <= peso_maximo:  
            itens_escolhidos.append((nome, peso, valor))
            peso_atual += peso
            valor_total += valor
        else:
            break

    return valor_total, itens_escolhidos

