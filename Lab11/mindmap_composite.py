import os

class MindMapComposite:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def get_shape_representation(self, shape):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, "{}")

    def display(self, indent=0):
        if indent == 0:
            print("mindmap" + os.linesep + "  root", end="")

        print("  " * indent + str(self))
        indent += 2
        for child in self.children:
            child.display(indent + 2)

    def __str__(self):
        shape_representation = self.get_shape_representation(self.name)
        return shape_representation.format(self.name)
