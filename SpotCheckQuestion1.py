#Harry Derouich
#09/12/14
#Functions Spot Check - Question 1a

def get_info():
    password = input("Please enter your password, between 8 and 16 characters: ")
    return password

def validation(password):
    length = len(password)
    while length < 8 or length > 16:
        if length > 16:
            print("Password too long")
            print()
            password = input("Please enter your password, between 8 and 16 characters: ")
            length = len(password)
        elif length < 8:
            print("Password too short")
            print()
            password = input("Please enter your password, between 8 and 16 characters: ")
            length = len(password)
    print("Password Accepted")
    return length

def password_checker():
    password = get_info()
    validation(password)

password_checker()
