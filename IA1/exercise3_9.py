# student name: Nhu Tran
# email: ntran66@student.gsu.edu

''' Write a program to compare the cost of the packages. The program prompts the user to 
enter the weight and price of each package and then displays the one with the better price '''

pkg_1w = float(input('Enter package 1 weight (lbs): '))
pkg_1c = float(input('Enter package 1 cost: '))

pkg_2w = float(input('Enter package 2 weight (lbs): '))
pkg_2c = float(input('Enter package 2 cost: '))


if pkg_1w/pkg_1c > pkg_2w/pkg_2c:
    print("Package 1 have better price")
elif pkg_1w/pkg_1c < pkg_2w/pkg_2c:
    print("Package 2 have better price")
else:
    print("Two packages have the same price")
