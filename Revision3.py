#Harry Derouich
#25/11/14
#Functions Class Exercises - Revision 3

def get_info():
    num1 = int(input("Please enter the 1st number: "))
    num2 = int(input("Please enter the 2nd number: "))
    return num1, num2

def ordering(num1, num2):
    if num1 > num2:
        num1 = str(num1)
        num2 = str(num2)
        output = num2 + " " + num1
    elif num1 < num2:
        num1 = str(num1)
        num2 = str(num2)
        output = num1 + " " + num2
    else:
        print("The numbers are the same")
    return output

def print_answer(output):
    print(output)

def main_prog():
    num1, num2 = get_info()
    output = ordering(num1, num2)
    print_answer(output)

main_prog()
