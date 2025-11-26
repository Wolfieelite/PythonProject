class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

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

    def display(self, indent = 0):

        print(" " * indent + str(self))

    def __str__(self):
        shape_representation = self.get_shape_representation(self.name)
        return shape_representation.format(self.name)
