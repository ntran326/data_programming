# Nhu Tran

def locateLargest(m):
    largest_x = 0
    largest_y = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > m[largest_x][largest_y]:
                largest_x, largest_y = i, j
    return largest_x, largest_y


def main():
    matrix = []
    numRows = int(input("Enter the number of rows in the list: "))

    for i in range(numRows):
        matrix.append([float(x.strip()) for x in input("Enter a row: ").split()])
    x, y = locateLargest(matrix)
    print("The location of the largest element is at ({}, {})".format(x, y))

main()