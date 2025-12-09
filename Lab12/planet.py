import turtle

class Planet:
    def __init__(self, name, radius, mass, distance, x, y, vx, vy, color):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance
        self.__x = x
        self.__vx = vx
        self.__y = y
        self.__vy = vy
        self.__color = color
        self.__t = turtle.Turtle()
        self.__t.color(self.__color)
        self.__t.shape("circle")
        self.__t.penup()
        self.__t.goto(self.__x, self.__y)
        self.__t.pendown()

    def get_mass(self):
        return self.__mass

    def distance(self):
        return self.__distance

    def get_pos_x(self):
        return self.__x

    def get_pos_y(self):
        return self.__y

    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def set_vx(self, new_vx):
         self.__vx = new_vx

    def set_vy(self, new_vy):
        self.__vy = new_vy

    def move_to(self, pos_x, pos_y):
        self.__x = pos_x
        self.__y = pos_y
        self.__t.goto(self.__x, self.__y)

    def __str__(self):
        return f'Name: {self.__name} {self.__x}, {self.__y}, Radius: {self.__radius} '


    def __eq__(self, other):
        return self.__name == other.__name