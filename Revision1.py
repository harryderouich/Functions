#Harry Derouich
#21/11/14
#Functions class exercises - Revision 1

def input_values():
    number = int(input("Please enter a number: "))
    character = str(input("Please enter a character: "))
    return number, character


def symbol_calc(number, character):
    total = number * character
    return total

def print_symbols(total):
    print(total)

def output_symbols():
    number, character = input_values()
    total = symbol_calc(number, character)
    print_symbols(total)

output_symbols()
