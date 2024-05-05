class Node:
    def __init__(self, name):
        self.name = name
        self.left = self
        self.right = self
        self.up = self
        self.down = self

class ColumnNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.size = 0

class DancingLinks:
    def __init__(self, matrix):
        self.header = self.create_dancing_links(matrix)

    def create_dancing_links(self, matrix):
        header = ColumnNode("header")
        nodes = []

        for col_index in range(len(matrix[0])):
            new_column = ColumnNode(col_index)
            header.left.right = new_column
            new_column.left = header.left
            new_column.right = header
            header.left = new_column

            for row_index in range(len(matrix)):
                if matrix[row_index][col_index] == 1:
                    new_node = Node((row_index, col_index))
                    nodes.append(new_node)
                    new_column.size += 1

                    current_column_node = new_column.up
                    while current_column_node != new_column:
                        current_column_node.down.up = new_node
                        new_node.down = current_column_node.down
                        current_column_node.down = new_node
                        new_node.up = current_column_node

                        current_column_node = current_column_node.up

        return header

    def cover(self, column_node):
        column_node.right.left = column_node.left
        column_node.left.right = column_node.right

        current_row_node = column_node.down
        while current_row_node != column_node:
            current_column_node = current_row_node.right
            while current_column_node != current_row_node:
                current_column_node.down.up = current_column_node.up
                current_column_node.up.down = current_column_node.down
                current_column_node.column.size -= 1

                current_column_node = current_column_node.right

            current_row_node = current_row_node.down

    def uncover(self, column_node):
        current_row_node = column_node.up
        while current_row_node != column_node:
            current_column_node = current_row_node.left
            while current_column_node != current_row_node:
                current_column_node.down.up = current_column_node
                current_column_node.up.down = current_column_node
                current_column_node.column.size += 1

                current_column_node = current_column_node.left

            current_row_node = current_row_node.up

        column_node.right.left = column_node
        column_node.left.right = column_node

    def solve_exact_cover(self, solution):
        if self.header.right == self.header:  
            return True

        column_node = self.choose_column_with_min_size()
        self.cover(column_node)

        current_row_node = column_node.down
        while current_row_node != column_node:
            solution.append(current_row_node.name[0])

            current_column_node = current_row_node.right
            while current_column_node != current_row_node:
                self.cover(current_column_node.column)
                current_column_node = current_column_node.right

            if self.solve_exact_cover(solution):
                return True

            solution.pop()
            column_node = current_row_node.column
            current_column_node = current_row_node.left
            while current_column_node != current_row_node:
                self.uncover(current_column_node.column)
                current_column_node = current_column_node.left

            current_row_node = current_row_node.down

        self.uncover(column_node)
        return False

    def choose_column_with_min_size(self):
        min_size = float('inf')
        chosen_column = None
        current_column = self.header.right

        while current_column != self.header:
            if current_column.size < min_size:
                min_size = current_column.size
                chosen_column = current_column
            current_column = current_column.right

        return chosen_column


matrix = [
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0]
]

exact_cover_solver = DancingLinks(matrix)
solution = []
if exact_cover_solver.solve_exact_cover(solution):
    print("Exact Cover Solution:", solution)
else:
    print("No solution found.")
