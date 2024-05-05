def reversed_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter a sentence:")

rs = reversed_sentence(input_sentence)

print("Original sentence:", input_sentence)
print("Reversed sentence without reversing words:", rs)