#Harry Derouich
#09/12/14
#Functions Spot Check - Question 3

def get_input():
    distance = float(input("Please enter the journey distance in miles: "))
    mpg = float(input("Please enter the MPG (Miles Per Gallon) of the vehicle: "))
    current_price = float(input("Please enter the current price of fuel in pence: "))
    return distance, mpg, current_price

def calculate_cost(distance, mpg, current_price):
     price_per_gallon = current_price * 4.55
     gallons_needed = distance / mpg
     cost = price_per_gallon * gallons_needed
     pounds = round(cost / 100, 2)
     return pounds

def display_cost(pounds):
    print("The total cost for the journey is: £{0}".format(pounds))

def journey_calc():
    distance, mpg, current_price = get_input()
    pounds = calculate_cost(distance, mpg, current_price)
    display_cost(pounds)

journey_calc()
