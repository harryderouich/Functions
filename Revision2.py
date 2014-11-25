#Harry Derouich
#25/11/14
#Functions class exercises - Revision 2
import string
def get_number():
    number = int(input("Please enter a number: "))
    return number

def odd_validate(number):
    if number % 2 == 0:
        number_odd = False
    else:
        number_odd = True
    return number_odd

def stars(number):
    while number >= 1:
        number = (number * "*")
        print("{0:^99}".format(stars, number))
        number = number - 2



