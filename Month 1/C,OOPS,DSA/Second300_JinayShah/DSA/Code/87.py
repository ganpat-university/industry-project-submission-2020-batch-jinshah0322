def compress_lzw(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_sequence = ""

    for char in data:
        current_sequence += char
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = next_code
            next_code += 1
            current_sequence = char

    if current_sequence in dictionary:
        result.append(dictionary[current_sequence])

    return result

def decompress_lzw(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []
    current_code = compressed_data[0]
    current_sequence = dictionary[current_code]

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_sequence + current_sequence[0]
        else:
            raise ValueError("Invalid compressed data")

        result.append(entry)
        dictionary[next_code] = current_sequence + entry[0]
        next_code += 1
        current_sequence = entry

    return ''.join(result)

# Example usage:
original_data = "ABABABABAABABA"
compressed_data = compress_lzw(original_data)
decompressed_data = decompress_lzw(compressed_data)

print("Original Data:", original_data)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
