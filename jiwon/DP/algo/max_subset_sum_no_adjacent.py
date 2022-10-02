def maxSubsetSumNoAdjacent(array):
    length = len(array)

    if length == 0:
        return 0
    elif length == 1:
        return array[0]

    dp = array[:]
    dp[1] = max(array[0], array[1]) # 두 번째 원소 DP = max(첫 번째 원소, 두 번째 원소)

    for i in range(2, length):
        dp[i] = max(dp[i-2] + array[i], dp[i-1])

    return dp[-1]
