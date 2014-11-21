#Harry Derouich
#14/11/14
#Functions starter exercise

def calculate_basic_pay(hours, rate):
    total = hours * rate
    return total

def calculate_overtime_pay(hours, rate):
    overtime_rate = rate * 1.5
    overtime_hours = hours - 40
    total = overtime_hours * overtime_rate + (40 * rate)
    return total

def work_details():
    hours = int(input("Please enter the total hours worked: "))
    rate = int(input("Please enter your basic rate of pay: "))
    return hours, rate

def calculate_total_pay(hours, rate):
    if hours <= 40:
        total = calculate_basic_pay(hours, rate)
    else:
        total = calculate_overtime_pay(hours, rate)
    return total

def display_total_pay(total):
    print(total)

def calculate_pay():
    hours, rate = work_details()
    total = calculate_total_pay(hours, rate)
    display_total_pay(total)

calculate_pay()



