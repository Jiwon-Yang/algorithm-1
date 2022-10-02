def levenshteinDistance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    dp = [[x for x in range(n)] for y in range(m)]

    for i in range(1, m):
        dp[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            if str1[i-1] == str2[j-1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j - 1][i], dp[j - 1][i - 1], dp[j][i - 1]) + 1

    return dp[m-1][n-1]

if __name__ == "__main__":
    levenshteinDistance("abc", "y")
