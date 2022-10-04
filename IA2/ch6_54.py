# Nhu Tran

def countLetters(s):
    count = 0
    for ch in s:
        count += 1
    return count

string = input('Enter a string: ')
remove_space = string.replace(" ", "")
print("Number of letters in string is", countLetters(remove_space))



