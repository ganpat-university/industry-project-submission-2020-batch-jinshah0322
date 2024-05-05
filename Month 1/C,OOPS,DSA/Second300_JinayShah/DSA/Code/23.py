def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def find_all_lcs(str1, str2, i, j, dp):
    if i == 0 or j == 0:
        return ['']

    if str1[i - 1] == str2[j - 1]:
        lcs_list = find_all_lcs(str1, str2, i - 1, j - 1, dp)
        return [lcs + str1[i - 1] for lcs in lcs_list]
    else:
        lcs_list = []
        if dp[i - 1][j] >= dp[i][j - 1]:
            lcs_list += find_all_lcs(str1, str2, i - 1, j, dp)
        if dp[i][j - 1] >= dp[i - 1][j]:
            lcs_list += find_all_lcs(str1, str2, i, j - 1, dp)
        return lcs_list

def print_all_lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    lcs_len = lcs_length(str1, str2)
    find_all_lcs(str1, str2, m, n, dp)
    
    lcs_list = find_all_lcs(str1, str2, m, n, dp)
    lcs_list = sorted(set(lcs_list))  

    print(f"Longest Common Subsequences in lexicographical order: {lcs_list}")


str1 = "abcabcaa"
str2 = "acbacba"
print_all_lcs(str1, str2)
