import turtle
from planet import Planet
from sun import Sun
from solar_system import SolarSystem

class Simulation:
    def __init__(self, solar_system:SolarSystem, width, height, number_periods):
        self.__solar_system = solar_system
        self.__width = width
        self.__height = height
        self.__number_periods = number_periods
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width=self.__width, height=self.__height)
        self.__screen.bgcolor("black")
        self.__t.clear()

    def run(self):
        print("running simulation")
        self.__solar_system.show_planets()
        for a_move in range(self.__number_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()
        self.freeze()

    def freeze(self):
        self.__screen.exitonclick()

if __name__ == '__main__':
    ss = SolarSystem()
    simulation = Simulation(ss, 500, 500, 2000)

    sol = Sun("SOL", 5000, 500000000000000, 320000, 0, 0)
    ss.add_sun(sol)

    earth = Planet("Earth", 30, 50, 75,0, 50, 50, 35, "Green")
    ss.add_planet(earth)

    simulation.run()