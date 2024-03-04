# task 1 Homework 27.02.2024

# current_value = float(input("awaiting value"))
#
# integer_1 = -273
# CONSTANT = (9/5)
# MY_CONSTANT = 32
# CONSTANT_1 = 273.15
# if current_value >= integer_1:
#
#     print (current_value * CONSTANT + MY_CONSTANT,"F")
#     print (current_value + CONSTANT_1,"K")
#
# else:
#     print ("error incorrect value")
#
# start_new_work = "enter"
#
# while start_new_work =="enter":
#
#     current_value = float(input("awaiting value"))
#
#     integer_1 = -273
#     CONSTANT = (9 / 5)
#     MY_CONSTANT = 32
#     CONSTANT_1 = 273.15
#     if current_value >= integer_1:
#
#         print(current_value * CONSTANT + MY_CONSTANT, "F")
#         print(current_value + CONSTANT_1, "K")
#
#     else:
#         print("error incorrect value")
#
#     start_new_work = "enter"

######################################################################

# #task 2 Homework 27.02.2024

# current_value_1 = float(input('awaiting value V1'))
#
# current_value_2 = float(input('awaiting value t1'))
#
# current_value_3 = float(input('awaiting value V2'))
#
# current_value_4 = float(input('awaiting value t2'))
#
# CONSTANT = 0
#
#
# integer = ((current_value_1 * current_value_2) + (current_value_3 * current_value_4))
#
# integer_2 = integer / (current_value_1 + current_value_3)
#
# if current_value_2 and current_value_4 >= CONSTANT:
#     print (integer_2)
# else:
#     print ("error unknown value")
#
# start_new_work = "enter"
# while start_new_work == "enter":
#
#     current_value_1 = float(input('awaiting value V1'))
#
#     current_value_2 = float(input('awaiting value t1'))
#
#     current_value_3 = float(input('awaiting value V2'))
#
#     current_value_4 = float(input('awaiting value t2'))
#
#     CONSTANT = 0
#
#     integer = ((current_value_1 * current_value_2) + (current_value_3 * current_value_4))
#
#     integer_2 = integer / (current_value_1 + current_value_3)
#
#     if current_value_2 and current_value_4 >= CONSTANT:
#         print(integer_2)
#     else:
#         print("error unknown value")
#
#     start_new_work = "enter"

###################################################################

# task 3 Homework 27.02.2024

hello = input("Welcome to calculator v1.2. For start press enter button!")

current_value_1 = float(input("Awaiting for first number"))
current_value_2 = float(input('Awaiting for second number'))
current_value_3 = input("Please choose basic calculator operations")

if current_value_3 =='+':
    print(current_value_1 + current_value_2)
if current_value_3 == "-":
    print(current_value_1 - current_value_2)
if current_value_3 == "*":
    print(current_value_1 * current_value_2)
if current_value_3 == "/":
    print(current_value_1 / current_value_2)


Start_new_calculator_operations = 'enter'

while Start_new_calculator_operations =='enter':

    current_value_1 = float(input("Awaiting for first number"))
    current_value_2 = float(input('Awaiting for second number'))
    current_value_3 = input("Please choose basic calculator operations")

    if current_value_3 == '+':
        print(current_value_1 + current_value_2)
    if current_value_3 == "-":
        print(current_value_1 - current_value_2)
    if current_value_3 == "*":
        print(current_value_1 * current_value_2)
    if current_value_3 == "/":
        print(current_value_1 / current_value_2)