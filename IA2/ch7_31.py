# Nhu Tran

def count(s):

	counts = [0] * len(s)

	for i in range(0, len(s)):
		if s[i].isdigit():
			counts[int(s[i])] += 1

	for i in range(0, len(counts)):
		if counts[i] != 0:
			print(i, "occurs", counts[i], "time.")

string = input('Enter a string: ')
count(string)

 
    
    

