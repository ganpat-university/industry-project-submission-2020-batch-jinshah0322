class Node:
    def __init__(self, start, end=None):
        self.start = start
        self.end = end if end is not None else float('inf')  
        self.children = {}
        self.suffix_link = None

def ukkonen_suffix_tree_construction(text):
    text += '$'
    root = Node(-1)
    active_node = root
    active_edge = 0
    active_length = 0
    remaining_suffixes = 0

    for i in range(len(text)):
        remaining_suffixes += 1
        last_created_node = None

        while remaining_suffixes > 0:
            if active_length == 0:
                active_edge = i

            if text[i] not in active_node.children:
                active_node.children[text[i]] = Node(i)
                if last_created_node is not None:
                    last_created_node.suffix_link = active_node
                    last_created_node = None
            else:
                next_node = active_node.children[text[i]]
                edge_length = min(next_node.end, i) - next_node.start + 1  

                if active_length >= edge_length:
                    active_edge += edge_length
                    active_length -= edge_length
                    active_node = next_node
                    continue

                if text[next_node.start + active_length] == text[i]:
                    active_length += 1

                    if last_created_node is not None and active_node != root:
                        last_created_node.suffix_link = active_node
                        last_created_node = None

                    break

                new_node = Node(next_node.start, next_node.start + active_length - 1)
                active_node.children[text[i]] = new_node
                next_node.start += active_length
                new_node.children[text[next_node.start]] = next_node

                if last_created_node is not None:
                    last_created_node.suffix_link = new_node

                last_created_node = new_node

            remaining_suffixes -= 1

            if active_node == root and active_length > 0:
                active_length -= 1
                active_edge = i - remaining_suffixes + 1
            elif active_node != root:
                active_node = active_node.suffix_link

    return root

def print_suffix_tree(node, text, depth=0):
    for child_char, child_node in node.children.items():
        edge_label = text[child_node.start:min(child_node.end + 1, len(text))]
        print("  " * depth + f"Edge: {edge_label} from {child_node.start} to {child_node.end}")
        print_suffix_tree(child_node, text, depth + 1)

text = "banana"
suffix_tree_root = ukkonen_suffix_tree_construction(text)
print("Suffix Tree:")
print_suffix_tree(suffix_tree_root, text)
