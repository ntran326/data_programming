# student name: Nhu Tran
# email: ntran66@student.gsu.edu

# Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total.

subtotal = float(input("Enter subtotal: "))
grat_rate = float(input("Enter gratuity rate: "))

grat_tot = subtotal * grat_rate/100
total = subtotal + grat_tot

print('gratuity is' , grat_tot , 'and the total is' , total)