import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char=None, frequency=None):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(text):
    frequency_counter = Counter(text)
    priority_queue = [HuffmanNode(char, frequency) for char, frequency in frequency_counter.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(frequency=left_node.frequency + right_node.frequency)
        internal_node.left = left_node
        internal_node.right = right_node

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)

def huffman_encode(text):
    if not text:
        return None

    root = build_huffman_tree(text)
    codes = {}
    build_huffman_codes(root, "", codes)

    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

text_to_compress = "this is an example for huffman encoding"
encoded_text, huffman_codes = huffman_encode(text_to_compress)

print("Original text:", text_to_compress)
print("Encoded text:", encoded_text)
print("Huffman codes:", huffman_codes)