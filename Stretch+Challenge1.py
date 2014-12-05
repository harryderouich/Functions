#Harry Derouich
#05/12/14
#Functions Class Exercises - Stretch and Challenge 1

def get_info():
    print("'1' = Metres + centimetres --> Feet + inches")
    print("'2' = Feet + inches --> Metres + centimetres")
    measurement = int(input("Please enter 1 or 2: "))
    return measurement

def which_converter(measurement):
    if measurement == 1:
        metres, cm = get_metrescm()
        feet, inches = metric_to_imperial(metres, cm)
        unit1 = "m"
        unit2 = "cm"
        return feet, inches, unit1, unit2
    elif measurement == 2:
        feet, inches = get_feetinches()
        metres, cm = imperial_to_metric(feet, inches)
        unit1 = "'"
        unit2 = '"'
        return metres, cm, unit1, unit2
    else:
        print("Please enter 1 or 2")


def get_metrescm():
    metres = int(input("Please enter the number of metres: "))
    cm = int(input("Please enter the number of centimetres: "))
    return metres, cm

def get_feetinches():
    feet = int(input("Please enter the number of feet: "))
    inches = int(input("Please enter the number of inches: "))
    return feet, inches

def metric_to_imperial(metres, cm):
    #convert to smallest units (metres to centimetres)
    m_to_cm = metres * 100
    cm = cm + m_to_cm
    #convert all to inches
    inches = cm * 0.397
    #convert up to feet
    feet = int(inches // 12)
    inches = float(inches % 12)
    return feet, inches

def imperial_to_metric(feet, inches):
    #convert to smallest units (feet to inches)
    feet_to_inches = feet * 12
    inches = inches + feet_to_inches
    #convert all to centimetres
    cm = inches * 2.54
    #convert up to metres
    metres = int(cm // 100)
    cm = float(cm % 100)
    return metres, cm

def conversion():
    measurement = get_info()
    large_unit_value, small_unit_value, large_unit, small_unit = which_converter(measurement)
    print("The converted values are {0:.1f}{1} {2:.2f}{3}".format(large_unit_value, large_unit, small_unit_value, small_unit))

conversion()


    
