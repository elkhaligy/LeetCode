def minDistance(word1: str, word2: str) -> int:
    # 2D Dynamic programming, checkout the board for reference
    row_len = len(word2) + 1
    col_len = len(word1) + 1
    dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

    for i in range(row_len):
        for j in range(col_len):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else: 
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
                

    #print(dp)
    return dp[-1][-1]


print(minDistance(word1 = "zoologicoarchaeologist", word2 = "zoogeologist"))