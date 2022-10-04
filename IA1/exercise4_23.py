# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f 
and displays its corresponding numeric value 4, 3, 2, 1, or 0 '''

letter_grade = input('Enter a letter grade: ')

low_letter = letter_grade.lower()

if low_letter == 'f':
    print('0')
elif low_letter == 'd':
   print('1')
elif low_letter == 'c':
    print('2')
elif low_letter == 'b':
    print('3')
elif low_letter == 'a':
    print('4')
else:
    print("Invalid letter")

