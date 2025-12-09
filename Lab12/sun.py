import turtle
class Sun:

    def __init__(self, name, radius, mass, temp, x, y):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        self.__x = x
        self.__y = y
        self.__t = turtle.Turtle()
        self.__t.color("Orange")
        self.__t.shape("circle")
        self.__t.goto(self.__x, self.__y)

    def get_mass(self):
        return self.__mass

    def get_pos_x(self):
        return self.__x

    def get_pos_y(self):
        return self.__y

    def __str__(self):
        return f"Sun(name={self.__name}, temp={self.__temp}, mass={self.__mass}, x={self.__x}, y={self.__y})"