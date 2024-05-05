def word_break_backtrack(s, word_dict):
    def backtrack(start):
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and backtrack(end):
                return True

        return False

    return backtrack(0)


word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
input_string = "pineapplepenapple"

result = word_break_backtrack(input_string, word_dict)

if result:
    print("The input string can be segmented.")
else:
    print("The input string cannot be segmented.")
