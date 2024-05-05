def full_justify(words, max_width):
    result, current_line, current_length = [], [], 0

    for word in words:
        if current_length + len(word) + len(current_line) > max_width:
            for i in range(max_width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            result.append(''.join(current_line))
            current_line, current_length = [], 0

        current_line += [word]
        current_length += len(word)

    result.append(' '.join(current_line).ljust(max_width))
    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 14
result = full_justify(words, max_width)
for line in result:
    print(line)