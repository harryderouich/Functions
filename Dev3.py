#Harry Derouich
#28/11/14
#Functions Class Exercises - Development 3

def get_currencies():
    currency_from = int(input("Please enter the currency you want to change FROM, 1 = Euro, 2 = US Dollar, 3 = British Pound"))
    currency_to = int(input("Please enter the currency you want to change TO, 1 = Euro, 2 = US Dollar, 3 = British Pound"))
    print("Thank you!")
    return currency_from, currency_to

def what_calc(currency_from):
    if currency_from == 1:
        euro_calc(currency_to)
    elif currency_from == 2:
        dollar_calc(currency_from)
    elif currency_from == 3:
        pounds_calc(currency_from)

def euro_calc(currency_to):
        if currency_to == 1:
            #Euro to Euro (Please try again)
            print("You cannot convert Euro to Euro, Please try again")
        elif currency_to == 2:
            #Euro to USD
            value = float(input("Please enter the number of euros: €"))
            total = value * 1.302
        elif currency_to == 3:
            #Euro to GBP
            value = float(input("Please enter the number of euros: €"))
            total = value * 0.814
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")
        return total

def dollar_calc(currency_to):
        if currency_to == 1:
            #USD to Euro
            value = float(input('Please enter the number of dollars: $'))
            total = value * 0.768
        elif currency_to == 2:
            #USD to USD (Please try again)
            print("You cannot convert USD to USD, Please try again")
        elif currency_to == 3:
            #USD to GBP
            value = float(input('Please enter the number of dollars: $'))
            total = value * 0.625
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")
        return total

def pounds_calc(currency_to):
        if currency_to == 1:
            #GBP to Euro
            value = float(input("Please enter the number of pounds: £"))
            total = value * 1.229
        elif currency_to == 2:
            #GBP to USD
            value = float(input("Please enter the number of pounds: £"))
            total = value * 1.601
        elif currency_to == 3:
            #GBP to GBP (Please try again)
            print("You cannot convert GBP to GBP, Please try again")
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")
        return total


