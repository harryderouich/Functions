#Harry Derouich
#28/11/14
#Functions Class Exercises - Revision 4

def get_info():
    degrees_f = float(input("Please enter the temperature in °F: "))
    return degrees_f

def calc_F_to_C(degrees_f):
    degrees_c = ((degrees_f - 32) * (5/9))
    return degrees_c

def temp_calculator():
    degrees_f = get_info()
    degrees_c = calc_F_to_C(degrees_f)
    degrees_c = round(degrees_c, 2)
    print("The converted temperature is {0}°C".format(degrees_c))

temp_calculator()
