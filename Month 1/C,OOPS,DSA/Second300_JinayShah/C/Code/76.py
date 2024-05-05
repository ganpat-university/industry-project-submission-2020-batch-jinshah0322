from suffix_trees import STree

def build_suffix_tree(s):
    return STree.STree(s)

text = "banana"
suffix_tree = build_suffix_tree(text)
print("Suffix Tree:", suffix_tree.word)