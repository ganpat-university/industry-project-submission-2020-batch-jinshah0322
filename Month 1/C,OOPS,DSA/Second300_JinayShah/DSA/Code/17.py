def power_set_lexico_order(input_set):
    n = len(input_set)
    power_set = []

    for i in range(2**n):
        subset = [input_set[j] for j in range(n) if (i & (1 << j)) > 0]
        power_set.append(subset)

    power_set.sort()  
    return power_set


input_set = [1, 2, 3]
result = power_set_lexico_order(input_set)
print("Power Set in Lexicographic Order:", result)
