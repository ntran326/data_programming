# Nhu Tran

def sumMajorDiagonal(m):
    sum = 0

    for i in range(len(m)):
        sum += m[i][i]
    return sum

def main():
    input_matrix = []
    number_of_rows = 4
    number_of_columns = 4

    for j in range(number_of_rows):
        input_string = input('Enter a 4-by-4 matrix row for row ' + str(j+1) + ": ")
        items = input_string.split()
        number_list = [eval(x) for x in items]
        input_matrix.append(number_list)

    print("\n\nSum of the elements in the major diagonal is", sumMajorDiagonal(input_matrix))

main()