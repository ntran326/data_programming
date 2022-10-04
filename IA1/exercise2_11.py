# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program that prompts the user to enter the final account value, the annual interest rate
in percent, and the number of years, and then displays the initial deposit amount '''

final_acc = float(input('Enter the final account value: '))
annual_rate = float(input('Enter the annual interest rate: ')) / 1200
years = int(input('Enter the number of years: ')) * 12

initial = final_acc / (1 + annual_rate) ** years

print('The initial investment value is' , round(initial,2))

