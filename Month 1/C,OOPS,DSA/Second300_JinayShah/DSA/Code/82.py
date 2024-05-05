class CacheObliviousNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

def cache_oblivious_search(tree, key):
    return _cache_oblivious_search(tree, key)

def _cache_oblivious_search(node, key):
    if not node:
        return None

    i = 0
    while i < len(node.keys) and key > node.keys[i]:
        i += 1

    if i < len(node.keys) and key == node.keys[i]:
        return node.keys[i]

    if not node.children:
        return None

    return _cache_oblivious_search(node.children[i], key)

def cache_oblivious_insert(tree, key):
    if not tree:
        return CacheObliviousNode(keys=[key])

    return _cache_oblivious_insert(tree, key)

def _cache_oblivious_insert(node, key):
    i = 0
    while i < len(node.keys) and key > node.keys[i]:
        i += 1

    if i < len(node.keys) and key == node.keys[i]:
        return node  

    if not node.children:
        node.keys.insert(i, key)
    else:
        child = _cache_oblivious_insert(node.children[i], key)
        if len(child.keys) > 2 * len(node.keys):
            node.keys.insert(i, child.keys.pop())
            node.children.insert(i + 1, child)

    return node


cob_tree = CacheObliviousNode(keys=[5, 10, 15])
cache_oblivious_insert(cob_tree, 7)
cache_oblivious_insert(cob_tree, 12)

result = cache_oblivious_search(cob_tree, 7)
print(result)  
