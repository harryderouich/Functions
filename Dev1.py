#Harry Derouich
#28/11/14
#Functions Class Exercises - Development 1

def get_info():
    hours = int(input("Please enter the number of whole hours: "))
    mins = int(input("Please enter the number of whole minutes: "))
    secs = int(input("Please enter the number of remaining seconds: "))
    return hours, mins, secs

def calculations(hours, mins, secs):
    hours_to_mins = hours * 60
    mins = mins + hours_to_mins
    mins_to_secs = mins * 60
    secs = secs + mins_to_secs
    return secs

def total_calculator():
    hours, mins, secs = get_info()
    if mins > 60 or secs > 60:
        print("Please enter correct values for mins and secs and round up where possible")
    else:
        total = calculations(hours, mins, secs)
        print("The time in seconds is: {0}".format(total))

total_calculator()
