# Program to count Even and Odd numbers in a List

# list of numbers

even_count = 0
odd_count = 0

# iterating each number in list
for num in range(1, 100):

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

def closest_to_zero(numbers):
    length = len(numbers)
    if(length == 0):
        return 0

    closest= numbers[0]
    for num in range(length-1):
        number = numbers[num]
        abs_number = abs(number)
        abs_closest = abs(closest)

        if (abs_number < abs_closest):
            closest = number
        elif (abs_number == abs_closest and closest < 0):
            closest = number

    return abs(closest)


items = [7,-10, 13, 8, 4, -7.2,-12,-3.7,3.5,-9.6, 6.5,-1.7, -6.2,7]

print(closest_to_zero(items))

import sys
max_num = sys.maxsize
print(max_num)




