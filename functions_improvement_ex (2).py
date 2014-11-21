# functions improvement exercise
# times-table tester
import random


def information_collection():
    test_table = int(input("Which times-table do you want to be tested on? "))
    return test_table

def number_generator():
    number = random.randrange(2,13)
    return number

def print_statement(test_table, number):
    answer = int(input("{0}  x  {1}  =  ? ".format(test_table, number)))
    return answer

def check_statement(answer, test_table, number):
    if answer == test_table * number:
        print("Well done, you got the correct answer!")
        print()
    else:
        print("Sorry, you got the answer wrong, the correct answer is", answer)

def times_table_tester(test_table, number, answer):
    information_collection()
    number_generator()
    print_statement(test_table, number)
    check_statement(answer, test_table, number)

times_table_tester()


### main program
##print("Times-table tester")
##print()
##testTable = input("Which times-table do you want to be tested on? ")
##testTable = int(testTable)
##for questions in range(1,6):
##    Num1 = testTable
##    Num2 = random.randrange(2,13)
##    Ans = Num1 * Num2
##    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
##    UserAnswer = int(UserAnswer)
##    if UserAnswer == Ans:
##        print('Well done, you got the correct answer!')
##        print()
##    else:
##        print('Sorry, you got the answer wrong. The correct answer is',Ans)
##        print()
              
