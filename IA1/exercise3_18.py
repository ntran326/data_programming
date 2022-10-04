# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program that prompts the user to enter the currency exchange rate 
between U.S. dollars and Chinese Renminbi (RMB)'''

print(
'''
Pick 1 or 2 for currency exchange: 
1. U.S Dollar to Chinese Renminbi (RMB)
2. Chinese Renminbi (RMB) to U.S Dollar
'''
)

choice = int(input('Type in your choice: '))

if choice == 1:
    dollar = float(input('Enter U.S Dollar: '))
    to_RMB = dollar * 6.94
    print(dollar , 'dollar is' , to_RMB, 'RMB')
elif choice == 2:
    RMB = float(input('Enter Chinese Renminbi: '))
    to_dollar = RMB * 0.14
    print(RMB , 'Chinese Renminbi is' , round(to_dollar,3), 'U.S Dollar')
else:
    print('Invalid choice')
