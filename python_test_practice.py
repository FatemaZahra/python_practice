# create a function called user_name
# def user_name():

# How would you iterate over the following list: arr = [1,2,3,4,5]?
# display list help of for loop and if statement
# list = [1,2,3,4,5]
# length = len(list)
# for num in range(length):
#     print(list[num])

# and is the correct operator

# What is the diff between tuple and a list:
# a tuple is immutable syntax () whereas a list is mutable

#could you add an element in a tuple? no

#can you have multiple types of data in a tuple? yes

# data_type = {"0":0, "1":1, "2":2} --> dictionary

#how to create an object of a class DevOps

#devops_object = DevOps()

#adds 5 to the following list?
# arr = [1, 2, 3, 4]
# arr.append(5)
# print(arr)

# using a function that takes 1 arg, return True if arg is equal; to devops otherwise False
# def devops(choice):
#     choice_case = choice.lower()
#     if choice_case == "devops":
#         return True
#     else:
#         return False
#
# print(devops("DEvops"))

# how to inherit a class - write the correct syntax if you had class Y and class Z - inherit class z FROM CLASS y

# class Y(Z):

# HOW TO DECLARE SUPER
# super().__init__()

#a function should return True if value is contained in [list] at an even index, False otherwise
def even_index(list, value):
    length= len(list)
    for num in range(length):
        if list[num] == value and num % 2 == 0:
            return True
        else:
            return False

print(even_index([1,3,4,5],1))




# create 4 functions that take 2 args each function
# percentage(value1, value 2)
# divide
# calculate  DOB
# multiply
# in each function check to ensure the value entered is not 0
# each function must return correct mathematical value
def percentage(value1, value2):
    return (value1/value2)*100
print(percentage(2,5))

def divide(value1, value2):
    return value1/value2
print(divide(2,6))

from datetime import date
def date_of_birth(age):
    year = 2022 - age
    return year
print(date_of_birth(8))


# searching odd and even numbers using a function that has an argument of ints using range()
def searching_odd_even():
    even_list = []
    odd_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list
#create a function to claculate total value of shopping bill
# shopping_list = {5 items with values 3.4,5.5, 6, 7 in a key value format}
#must return the total amount

shopping_cart ={
    "a": 3.4,
    "b": 5.5,
    "c": 6,
    "d":7,
    "e":8
}

print(sum(shopping_cart.values()))

