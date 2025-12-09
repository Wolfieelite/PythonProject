import math
from gravity import Gravity
from planet import Planet
from sun import Sun

class SolarSystem:
    def __init__(self):
        self.__sun: Sun = None
        self.__planets: list[Planet] = []

    def add_sun(self, sun):
        self.__sun = sun

    def add_planet(self, new_planet: Planet):
        print("added planets")
        if new_planet not in self.__planets:
            self.__planets.append(new_planet)
        else:
            print("God said there cannot be 2 of those kind")

    def show_planets(self) -> None:
        for planet in self.__planets:
            print(planet)


    def move_planets(self):
        dt = .001  # Constant time interval for each solar system iteration.

        for planet in self.__planets:
            planet.move_to(
                planet.get_pos_x() + dt * planet.get_vx(),
                planet.get_pos_y() + dt * planet.get_vy())

            dist_x = self.__sun.get_pos_x() - planet.get_pos_x()
            dist_y = self.__sun.get_pos_y() - planet.get_pos_y()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            acc_x = Gravity.G * self.__sun.get_mass() * dist_x / new_distance ** 3
            acc_y = Gravity.G * self.__sun.get_mass() * dist_y / new_distance ** 3

            planet.set_vx(planet.get_vx() + dt * acc_x)
            planet.set_vy(planet.get_vy() + dt * acc_y)