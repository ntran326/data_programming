# student name: Nhu Tran
# email: ntran66@student.gsu.edu


''' write a program that prompts the user to enter a temperature and a wind speed. The program displays the
wind-chill temperature if the input is valid; otherwise, it displays a message indicating whether 
the temperature and/or wind speed is invalid '''

temp = float(input('Enter wind-chill temperature between -58F and 41F: '))



if temp in range(-58, 42):
    speed = float(input('Enter a wind speed <=2: '))
    if (speed <= 2):
        wind_chill_index = 25.74 + 0.6215 * temp - 35.75 * speed ** 0.16
        # print('The wind chill index is' , round(wind_chill_index, 3))
        print(f'The wind chill index is {round(wind_chill_index)}')
    else:
        print('invalid wind speed')
else:
    print('invalid temperature')
