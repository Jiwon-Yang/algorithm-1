def minNumberOfCoinsForChange(n, coins):
    coinsNum = [float("inf") for amount in range(n+1)]
    coinsNum[0] = 0
    for coin in coins:
        for amount in range(len(coinsNum)):
            if coin <= amount:
                coinsNum[amount] = min(
                    coinsNum[amount], coinsNum[amount-coin] + 1)
    return coinsNum[n] if coinsNum[n] != float("inf") else - 1
