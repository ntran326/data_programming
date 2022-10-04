# Nhu Tran

import random

def main():

    count = dict()
    
    for i in range(1000):
        num = random.randint(0,9) 
        count[num] = count.get(num,0) + 1
        
    for x, y in sorted(count.items()):
      print(x," : ", y)

main()