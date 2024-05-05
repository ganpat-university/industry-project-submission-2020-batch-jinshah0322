class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def do_rectangles_overlap(rect1, rect2):
    x_overlap = not (rect1.x + rect1.width < rect2.x or rect2.x + rect2.width < rect1.x)

    y_overlap = not (rect1.y + rect1.height < rect2.y or rect2.y + rect2.height < rect1.y)

    return x_overlap and y_overlap

# Example usage
rectangle1 = Rectangle(x=0, y=0, width=3, height=3)
rectangle2 = Rectangle(x=2, y=2, width=3, height=3)

if do_rectangles_overlap(rectangle1, rectangle2):
    print("Rectangles overlap.")
else:
    print("Rectangles do not overlap.")
