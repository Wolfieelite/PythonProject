import math

name = "Chris"
age = 21
height = 6.1
favorite_color = ["green", "blue", "purple", "orange"]


# print technique for vairable values:
print(name)
print(age)
print(height)
print(favorite_color)


print(f"Hello world! My name is {name} and I am {age} years old. My favorite color is {favorite_color[2]}")
print(f"""
name: {name}

Age: {age}
""")

circle_area = 5
print(float(circle_area))


print(math.sqrt(age))
print(math.sin(height))
print(math.cos(height))

fahrenheit = input("Enter degrees")
celsius = (int(fahrenheit) - 32) * 5/9
print(f"It is {fahrenheit}\N{DEGREE SIGN} Fahrenheit, which is {celsius}\N{DEGREE SIGN} Celsius")