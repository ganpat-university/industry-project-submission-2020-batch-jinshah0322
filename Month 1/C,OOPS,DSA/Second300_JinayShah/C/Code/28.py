def longest_palindromic_substring(s):
    processed_s = '#'.join('^{}$'.format(s))

    n = len(processed_s)
    p = [0] * n 
    center, right = 0, 0 

    for i in range(1, n - 1):
        mirror = 2 * center - i 

        if i < right:
            p[i] = min(right - i, p[mirror])

        while processed_s[i + p[i] + 1] == processed_s[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len, center_index = max((length, index) for index, length in enumerate(p))

    start = (center_index - max_len) // 2
    end = start + max_len

    return s[start:end]

input_string = "babad"
result = longest_palindromic_substring(input_string)
print("Longest Palindromic Substring:", result)