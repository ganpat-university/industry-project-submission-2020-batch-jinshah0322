def is_palindrome(s):
    return s == s[::-1]

def generate_partitions(input_str):
    n = len(input_str)
    result = []

    for i in range(1 << (n - 1)):
        current_partition = []
        start = 0
        for j in range(1, n):
            if (i & (1 << (j - 1))) != 0:
                current_partition.append(input_str[start:j])
                start = j
        current_partition.append(input_str[start:])

        if all(is_palindrome(part) for part in current_partition):
            result.append(current_partition)

    return result


input_str1 = "nitin"
result1 = generate_partitions(input_str1)
print(f"Palindromic Partitions for {input_str1}: {result1}")

input_str2 = "geeks"
result2 = generate_partitions(input_str2)
print(f"Palindromic Partitions for {input_str2}: {result2}")
