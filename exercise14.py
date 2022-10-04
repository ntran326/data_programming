# Nhu Tran

'''
Write a program that prompts the user to enter a text file and reads words
from the file and displays all the nonduplicate words in ascending order.
'''


def main():
    f_name = input('Enter file name: ')
    f_open = open(f_name,'r').readlines()

    newList = f_open[0].split()
    newList = ' '.join(filter(str.isalnum, newList)).split()

    seen = set()
    result = set()

    for x in newList:
        if x not in seen:
            seen.add(x)
            result.add(x)
        else:
            result.discard(x)
        
    print(sorted(list(result)))

main()