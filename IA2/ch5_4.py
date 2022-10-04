# Nhu Tran

def main():
    conversion = 1.609
    
    mile = 1
    count = 0
    print('miles' , '\t' , 'kilometers')

    while count < 10:
        count += 1
        mile = count * conversion
        print(count, '\t' , mile)
    
main()