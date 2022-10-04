# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program that prompts the user to enter a temperature between and 41°F,
 a wind speed greater than or equal to 2 , and then displays the wind-chill temperature'''

tempt = float(input("Enter a temperature in Fahrenheit between -58 and 41: "))
wind_speed = float(input("Enter the wind speed (>=2) in miles per hour: "))

wind_chill_index = 25.74 + 0.6215 * tempt - 35.75 * wind_speed ** 0.16

print('The wind chill index is' , round(wind_chill_index, 3))