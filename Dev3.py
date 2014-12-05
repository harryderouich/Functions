#Harry Derouich
#28/11/14
#Functions Class Exercises - Development 3

def get_currencies():
    currency_from = int(input("Please enter the currency you want to change FROM, 1 = Euro, 2 = US Dollar, 3 = British Pound, or enter 4 if you wish to perform many calculations: "))
    currency_to = int(input("Please enter the currency you want to change TO, 1 = Euro, 2 = US Dollar, 3 = British Pound: "))
    print("Thank you! Calculating that for you now")
    print()
    return currency_from, currency_to

def what_calc(currency_from):
    if currency_from == 1:
        euro_calc(currency_to)
    elif currency_from == 2:
        dollar_calc(currency_to)
    elif currency_from == 3:
        pounds_calc(currency_to)
    else:
        print("Please enter one of the currencies from 1-3. Thank you.")

def euro_calc(currency_to):
        if currency_to == 1:
            #Euro to Euro (Please try again)
            print("You cannot convert Euro to Euro, Please try again")
        elif currency_to == 2:
            #Euro to USD
            value = float(input("Please enter the number of euros: €"))
            total = value * 1.302
            print("Your conversion is: €{0:.2f} = ${1:.2f}".format(value, total))
        elif currency_to == 3:
            #Euro to GBP
            value = float(input("Please enter the number of euros: €"))
            total = value * 0.814
            print("Your conversion is: €{0:.2f} = £{1:.2f}".format(value, total))
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")


def dollar_calc(currency_to):
        if currency_to == 1:
            #USD to Euro
            value = float(input('Please enter the number of dollars: $'))
            total = value * 0.768
            print("Your conversion is: ${0:.2f} = €{1:.2f}".format(value, total))
        elif currency_to == 2:
            #USD to USD (Please try again)
            print("You cannot convert USD to USD, Please try again")
        elif currency_to == 3:
            #USD to GBP
            value = float(input('Please enter the number of dollars: $'))
            total = value * 0.625
            print("Your conversion is: ${0:.2f} = £{1:.2f}".format(value, total))
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")


def pounds_calc(currency_to):
        if currency_to == 1:
            #GBP to Euro
            value = float(input("Please enter the number of pounds: £"))
            total = value * 1.229
            print("Your conversion is: £{0:.2f} = €{1:.2f}".format(value, total))
        elif currency_to == 2:
            #GBP to USD
            value = float(input("Please enter the number of pounds: £"))
            total = value * 1.601
            print("Your conversion is: ${0:.2f} = ${1:.2f}".format(value, total))
        elif currency_to == 3:
            #GBP to GBP (Please try again)
            print("You cannot convert GBP to GBP, Please try again")
        else:
            #Must be 1-3
            print("Please enter one of the currencies from 1-3")

##def more_calcs():
##    currency_from = int(input("Please enter the currency you want to change FROM, 1 = Euro, 2 = US Dollar, 3 = British Pound: "))
##    currency_to = int(input("Please enter the currency you want to change TO, 1 = Euro, 2 = US Dollar, 3 = British Pound: "))
##    how_many = int(input("Please enter the number of calculations you wish to do: "))
##    if currency_from == 1:
##        title1 = "Euros"
##    elif currency_from == 2:
##        title1 = "USD"
##    elif currency_from == 3:
##        title1 = "GBP"
##    else:
##        title1 = "Error"
##    if currency_to == 1:
##        title2 = "Euros"
##    elif currency_to == 2:
##        title2 = "USD"
##    elif currency_to == 3:
##        title2 = "GBP"
##    else:
##        title2 = "Error"
##    for count in range(how_many):
##        value = int(input("Please enter the value: "))
##        if currency_from == 1:
##            if currency_to == 1:
##                #Euro to Euro (Please try again)
##                print("You cannot convert Euro to Euro, Please try again")
##            elif currency_to == 2:
##                #Euro to USD
##                total = value * 1.302
##            elif currency_to == 3:
##                #Euro to GBP
##                total = value * 0.814
##            else:
##                #Must be 1-3
##                print("Please enter one of the currencies from 1-3")
##        elif currency_from == 2:
##            if currency_to == 1:
##                #USD to Euro
##                total = value * 0.768
##            elif currency_to == 2:
##                #USD to USD (Please try again)
##                print("You cannot convert USD to USD, Please try again")
##            elif currency_to == 3:
##                #USD to GBP
##                total = value * 0.625
##            else:
##                #Must be 1-3
##                print("Please enter one of the currencies from 1-3")
##        elif currency_from == 3:
##            if currency_to == 1:
##                #GBP to Euro
##                total = value * 1.229
##            elif currency_to == 2:
##                #GBP to USD
##                total = value * 1.601
##            elif currency_to == 3:
##                #GBP to GBP (Please try again)
##                print("You cannot convert GBP to GBP, Please try again")
##            else:
##                #Must be 1-3
##                print("Please enter one of the currencies from 1-3")
##        else:
##            print("Error")
##        print("|{0:^5}|{1:^5}|".format(title1, title2))
##        total = round(total, 2)
##        print("|{0:^5}|{1:^5}|".format(value, total))
##    print("Thankyou for using the conversion, have a nice day!")
##    
            
            
        
        

    
            

currency_from, currency_to = get_currencies()
what_calc(currency_from)


    
    
