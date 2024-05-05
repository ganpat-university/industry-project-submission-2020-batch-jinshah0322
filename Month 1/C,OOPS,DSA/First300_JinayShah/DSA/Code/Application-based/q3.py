class FileSystemNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

def display_structure(node, indent=""):
    print(indent + node.name + ("/" if node.is_directory else ""))
    for child in node.children:
        display_structure(child, indent + "  ")

# Example usage:
if __name__ == "__main__":
    root = FileSystemNode("root", is_directory=True)
    documents = FileSystemNode("documents", is_directory=True)
    pictures = FileSystemNode("pictures", is_directory=True)
    report = FileSystemNode("report.txt")
    note = FileSystemNode("note.txt")

    root.children.extend([documents, pictures])
    documents.children.extend([report, note])

    display_structure(root)