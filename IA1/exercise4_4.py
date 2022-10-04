# student name: Nhu Tran
# email: ntran66@student.gsu.edu

# Write a program that prompts the user to enter the side of a hexagon and displays its area

from cmath import pi, tan
import math

side = float(input('Enter the side of a hexagon: '))

area = (6 * side ** 2) / (4 * tan(pi/6))

print(area)