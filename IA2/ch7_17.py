# Nhu Tran

def isAnagram(s1,s2):
    lst1 = []
    lst2 = []

    for x in s1:
        lst1.append(x)
    for x in s2:
        lst2.append(x)

    lst1.sort()
    lst2.sort()

    if (len(lst1) != len(lst2)):
        return False
    else:
        for x in range(len(lst1)):
            if (lst1[x] != lst2[x]):
                return False
        return True

def main():
    s1 = input('Enter first string: ')
    s2 = input('Enter second string: ')

    if (isAnagram(s1,s2)):
        print('The words', s1 , 'and' , s2 ,'are anagrams')
    else:
        print('The words', s1 , 'and' , s2 ,'are not anagrams')

main()