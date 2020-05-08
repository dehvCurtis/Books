# python3
# ex37 - create py program with each symbol or keyword

# Python Keywords
# def and_keyword():
#     var1 = 3
#     var2 = 9
#     if var1 and var2 <= 10:
#         print(f"{var1} and {var2} are less than or equal to 10")
# and_keyword()
#
# def as_keyword():
#     with open('/tmp/test.txt', 'w+') as file:
#         file.write("hello world")
# as_keyword()
#
# def assert_keyword(temp): # BROKEN
#     temp = 30
#     assert (temp <= 32),"Colder than freezing"
#     return ((temp-273)*1.8)+32
# assert_keyword()
#
# def break_keyword(): # BROKEN
#     var1 = "Python3"
#     for letter in var1:
#         print(letter)
#         if letter == "h":
#             break
# break_keyword()
#
# def class_keyword():
#     def func1():
#         print("func1")
#     def func2():
#         print("func2")
#     func1()
#     func2()
# class_keyword()
#
# def continue_keyword():
#     usr_input = input("Please enter a lower number less than 10 >")
#
#     usr_input = int(usr_input)
#
#     for i in range(usr_input, 11):
#         print(i)
#         i = i + 1
#         if i <= 11:
#             continue
#         else:
#             break
# continue_keyword()
#
# def func():
#     print("this is a function")
# func()
#
# def del_keyword():
#     dictionary = {"Test1":"Test_1","Test2":"Test_2"}
#     print(f"Printing dictionary: {dictionary}")
#     del dictionary['Test1']
#     print(f"Printing dictionary: {dictionary}")
#     dict.clear(dictionary)
#     print(f"Printing dictionary: {dictionary}")
#     del dictionary
# del_keyword()
#
# def if_elif_else_keyword():
#     hello = input("Hello there\n")
#     if hello == "hello":
#         print("Nice to meet you")
#         exit()
#     elif hello != "hello":
#         print("how rude")
#         exit()
#     else:
#         print("wut")
# if_elif_else_keyword()
#
# def except_keyword():
#     while True:
#         try:
#             x = int(input("Please enter a number: "))
#             break
#         except ValueError:
#             print("whoops, not a valid number")
# except_keyword()
#
# def exec_keyword():
#     import subprocess
#     exec("print(dir())")
# exec_keyword()
#
# def finally_keyword(x, y):
#     try:
#         quotient = x / y
#     except ZeroDivisionError:
#         print('division by zero!')
#     else:
#         print(f'the result is {quotient}')
#     finally:
#         print('finally clause')
#
# finally_keyword(10, 2)
#
# def for_keyword():
#     for num in range(0,11):
#         print(num)
#         num = num + 1
# for_keyword()
#
# from random import randint
# def from_keyword():
#     print(randint(0,25))
# from_keyword()
#
# def global_keyword():
#     global number
#     number = 15
# global_keyword()
# print(number)
#
# from random import randint
# rangeint = randint(0,10)
# def if_import_keywords():
#     if rangeint <= 5:
#         print(f'{rangeint} is less than or equal to 5')
#     elif rangeint >= 5:
#         print(f'{rangeint} greater than or equal to 5')
#     else:
#         print('sorry')
# if_import_keywords()
#
# def in_keyword():
#     for i in range(0,10):
#         print(i)
# in_keyword()
#
# def is_keyword():
#     if 1 is 1:
#         print('True')
#     else:
#         print('False')
# is_keyword()
#
# def lambda_keyword():
#     product = lambda x, y : x * y
#     print(product(2,6))
# lambda_keyword()
#
