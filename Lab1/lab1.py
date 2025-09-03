import math

# Problem 1:
circleRadius = 5
circleArea = math.pi * (circleRadius ** 2)
print("area of the circle with the radius of 5 is", circleArea)

sphereRadius = 3
sphereVolume = (4/3) * math.pi * (sphereRadius ** 3)
print("volume of the sphere with the radius of 3 is", sphereVolume)

triangleSideA = 3
triangleSideB = 4
triangleHypo = math.sqrt(triangleSideA * triangleSideB + triangleSideB * triangleSideA)
print("the hypotenuse of the triangle is ", triangleHypo)

# Problem 2
firstName = "chris"
lastName = "martetaylor"
fullName = firstName.capitalize() + " " + lastName.capitalize()
print(fullName)

# Problem 3
age = 21
height = 6.1
heightToInch = height * 12
weight = 170

print(type(age))
print(type(height))
print(type(weight))

BMI = (weight / heightToInch ** 2) * 703
# console.log("BMI is", BMI) (It was bound to happen eventually lol)
print("BMI is", BMI)