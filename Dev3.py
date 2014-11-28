#Harry Derouich
#28/11/14
#Functions Class Exercises - Development 3

def get_currencies():
    currency_from = int(input("Please enter the currency you want to change FROM, 1 = Euro, 2 = US Dollar, 3 = British Pound"))
    currency_to = int(input("Please enter the currency you want to change TO, 1 = Euro, 2 = US Dollar, 3 = British Pound"))
    print("Thank you!")
    return currency_from, currency_to

def calculations(currency_from, currency_to):
    if currency_from = 1: #Euro
        if currency_to = 1:
            #Euro to Euro (Please try again)
            print("You cannot convert Euro to Euro, Please try again")
        elif currency_to = 2:
            #Euro to USD
        elif currency_to = 3:
            #Euro to GBP
        else:
            #Must be 1-3
    elif currency_from = 2: #USD
        if currency_to = 1:
            #USD to Euro
        elif currency_to = 2:
            #USD to USD (Please try again)
            print("You cannot convert USD to USD, Please try again")
        elif currency_to = 3:
            #USD to GBP
        else:
            #Must be 1-3
    elif currency_from = 3: #GBP
        if currency_to = 1:
            #GBP to Euro
        elif currency_to = 2:
            #GBP to USD
        elif currency_to = 3:
            #GBP to GBP (Please try again)
            print("You cannot convert GBP to GBP, Please try again")
        else:
            #Must be 1-3

    return total
        
    
    
