def knapsack(peso_maximo, itens):
    n = len(itens)
    dp = [[0] * (peso_maximo + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        nome, peso, valor = itens[i - 1]
        for w in range(peso_maximo + 1):
            if peso <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso] + valor)
            else:
                dp[i][w] = dp[i - 1][w]

    valor_total = dp[n][peso_maximo]
    itens_escolhidos = []
    w = peso_maximo

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            itens_escolhidos.append(itens[i - 1])
            w -= itens[i - 1][1]
    
    return valor_total, itens_escolhidos
