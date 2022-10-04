# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program that prompts the user to enter a lowercase or uppercase letter and 
displays its corresponding number '''

user_input = str(input('Enter a lowercae or uppercase letter: '))

low_user = user_input.lower()

if low_user >= 'w':
    print('9')
elif low_user >= 't':
    print('8')
elif low_user >= 'p':
    print('7')
elif low_user >= 'm':
    print('6')
elif low_user >= 'j':
    print('5')
elif low_user >= 'g':
    print('4')
elif low_user >= 'd':
    print('3')
elif low_user >= 'a':
    print('2') 
else:
    print('invalid')