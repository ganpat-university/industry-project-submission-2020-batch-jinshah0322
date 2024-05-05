def word_break(word, word_dict):
    n = len(word)
    dp = [False] * (n + 1)  
    dp[0] = True  
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and word[j:i] in word_dict:
                dp[i] = True
                break  
    return dp[n]  

word = "leetcode"
word_dict = {"leet", "code"}

if word_break(word, word_dict):
    print(f"The word '{word}' can be segmented into valid words.")
else:
    print(f"The word '{word}' cannot be segmented into valid words.")