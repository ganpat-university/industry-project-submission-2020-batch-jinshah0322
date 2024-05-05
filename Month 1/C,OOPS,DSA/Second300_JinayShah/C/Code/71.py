def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current_code = 256
    current_sequence = ''

    for char in data:
        current_sequence += char
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = current_code
            current_code += 1
            current_sequence = char

    result.append(dictionary[current_sequence])
    return result

data = "ABABABABA"
compressed_data = lzw_compress(data)
print("LZW Compressed Data:", compressed_data)
