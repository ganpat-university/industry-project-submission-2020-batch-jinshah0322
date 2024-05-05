def process_queries(S, queries):
    result = []

    for query in queries:
        query_type, param = query

        if query_type == 1:
            index = param
            S = S[:index] + chr(ord(S[index]) + 1) + S[index + 1:]

        elif query_type == 2:
            length = param
            substring = S[:length]
            distinct_characters = len(set(substring))
            result.append(distinct_characters)

    return result


S1 = 'AABBBCCCC'
queries1 = [[1, 0], [2, 1], [1, 0], [2, 2], [1, 3]]
result1 = process_queries(S1, queries1)
print("Result 1:", result1)


S2 = 'XXYYY'
queries2 = [[1, 3], [2, 3], [1, 2]]
result2 = process_queries(S2, queries2)
print("Result 2:", result2)
