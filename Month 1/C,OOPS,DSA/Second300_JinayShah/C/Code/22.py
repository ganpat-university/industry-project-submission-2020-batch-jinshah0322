def lcs_three_strings(X, Y, Z):
  n, m, p = len(X), len(Y), len(Z)
  dp = [[[0 for _ in range(p + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      for k in range(1, p + 1):
        if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
          dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
        else:
          dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

  lcs_length = dp[n][m][p]

  return lcs_length

X = "ABCBDAB"
Y = "BDCABA"
Z = "ABCBAB"

lcs_length = lcs_three_strings(X, Y, Z)
print(f"Length of LCS: {lcs_length}")