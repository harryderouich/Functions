#Harry Derouich
#14/11/14
#Functions starter exercise

def calculate_basic_pay(hours, rate):
    total = hours * pay
    return total

def calculate_overtime_pay(hours, rate):
    overtime_rate = rate * 1.5
    overtime_hours = hours - 40
    total = overtime_hours * overtime_rate
    return total

def calculate_total_pay(hours, rate):
    if hours <= 40:
        total = calculate_basic_pay
    else:
        total = calculate_overtime_pay
    return total

def work_details():
    hours = int(input("Please enter the total hours worked: "))
    rate = int(input("Please enter your basic rate of pay: "))
    return hours
    return rate

def display_total_pay(calculate_total_pay):
    output = print(calculate_total_pay)
    return output

def calculate_pay():
    hours, rate = work_details()
    total_pay = calculate_total_pay(hours, rate)
    print(total_pay)

work_details()
total = calculate_total_pay(hours, rate)
print(total)


