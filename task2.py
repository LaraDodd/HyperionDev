"""This program calculates the areas that the foundations of a building covers"""
import math

shape = input("Please enter the shape of your building (square, rectangular or round): ")

if shape == "square":
    length = float(input("Please enter the length of your square foundation (metres): "))
    area = length**2
elif shape == "rectangular":
    width = float(input("Please enter the width of your rectangular foundation (metres): "))
    height = float(input("Please enter the width of your rectangular foundation (metres): "))
    area = width*height
else:
    radius = float(input("Please enter the radius of your circular based foundation (metres): "))
    area = math.pi*radius**2

print(f"The area taken up by the foundation of the building is {round(area, 2)} metres squared")

