#Harry Derouich
#14/11/14
#Functions starter exercise

basic_pay = int(input("Please enter your basic pay rate: £"))
overtime_pay = int(input("Please enter your overtime pay rate: £"))


hours_worked = int(input("Please enter the total number of basic hours worked: "))
overtime_hours_worked = int(input("Please enter the total number of overtime hours worked: "))

total_pay = (basic_pay * hours_worked) + (overtime_pay * overtime_hours_worked)

print("The total amount of pay is: £{0}".format(total_pay))
