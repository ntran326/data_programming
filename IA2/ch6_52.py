# Nhu Tran

def main():
    s1 = input("Enter the first string: ").rstrip()
    s2 = input("Enter the first string: ").rstrip()

    s3 = prefix(s1, s2)

    if s3 != None:
        print("The common prefix is " + s3)
    else:
        print("No common prefix");

def prefix(s1, s2):
    result = ""

    if len(s1)>len(s2): # let us reorder the strings by its length
        s1,s2=s2,s1
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            break;

    if len(result) == 0:
        return None
    else:
        return result

main()