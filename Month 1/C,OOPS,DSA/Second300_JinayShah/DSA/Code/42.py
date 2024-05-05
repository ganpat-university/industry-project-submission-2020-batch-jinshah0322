class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    
    char_freq = {}
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1

    
    priority_queue = [HuffmanNode(char, freq) for char, freq in char_freq.items()]

    
    while len(priority_queue) > 1:
        node1 = min(priority_queue, key=lambda x: x.freq)
        priority_queue.remove(node1)
        node2 = min(priority_queue, key=lambda x: x.freq)
        priority_queue.remove(node2)

        internal_node = HuffmanNode(freq=node1.freq + node2.freq)
        internal_node.left, internal_node.right = node1, node2

        priority_queue.append(internal_node)

    
    return priority_queue[0]

def build_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + "0", codes)
        build_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_compress(data):
    if not data:
        return None, None

    
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)

    
    compressed_data = "".join(codes[char] for char in data)

    return compressed_data, root

def huffman_decompress(compressed_data, root):
    if compressed_data is None or root is None:
        return None

    
    current_node = root
    decompressed_data = []

    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_data.append(current_node.char)
            current_node = root

    return "".join(decompressed_data)


data_to_compress = "abracadabra"
compressed_data, huffman_tree = huffman_compress(data_to_compress)
print("Compressed data:", compressed_data)

decompressed_data = huffman_decompress(compressed_data, huffman_tree)
print("Decompressed data:", decompressed_data)
