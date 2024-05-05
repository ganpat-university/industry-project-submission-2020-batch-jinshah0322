def first_non_repeating_char(input_str):
    char_count = {}
    char_index = {}

    # Traverse the string and populate the hash tables
    for i, char in enumerate(input_str):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_index[char] = i

    # Find the first non-repeating character
    result_index = float('inf')
    for char, count in char_count.items():
        if count == 1 and char_index[char] < result_index:
            result_index = char_index[char]

    return input_str[result_index] if result_index != float('inf') else None


input_string = "programming"
result = first_non_repeating_char(input_string)
if result is not None:
    print(f"The first non-repeating character in '{input_string}' is: {result}")
else:
    print(f"There is no non-repeating character in '{input_string}'.")