# Nhu Tran

l=[]

txt = input("Enter students' names and scores: ")

lst = txt.split()

for i in range(0,len(lst),2):
    sublist = []
    name = lst[i]
    score = int(lst[i+1])

    sublist.append(score)
    sublist.append(name)

    l.append(sublist)
    
l.sort()
print("Sorted list is: ")
for i in l:
    print(i[1],"  ",i[0])

