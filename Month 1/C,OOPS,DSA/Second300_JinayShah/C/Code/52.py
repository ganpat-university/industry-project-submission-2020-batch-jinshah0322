def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps_array(pattern)
    j = 0
    result = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            result.append(i - m + 1)
            j = lps[j - 1]

    return result

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)
print(f"Pattern found at indices: {result}")
