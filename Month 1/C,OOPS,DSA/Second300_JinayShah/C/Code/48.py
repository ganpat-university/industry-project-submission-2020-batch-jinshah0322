def longest_common_substring(str1, str2):
  n, m = len(str1), len(str2)
  dp = [[0] * (m + 1) for _ in range(n + 1)]
  max_length = 0
  lcs_end = 0  
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
        max_length = max(max_length, dp[i][j])
        lcs_end = i  
  lcs = str1[lcs_end - max_length:lcs_end]
  return max_length, lcs


str1 = "ABABC"
str2 = "BABCA"
max_length, lcs = longest_common_substring(str1, str2)
print("The length of the longest common substring is:", max_length) 
print("The longest common substring is:", lcs) 