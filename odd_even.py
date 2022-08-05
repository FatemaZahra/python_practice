# Program to count Even and Odd numbers in a List

# list of numbers

even_count = 0
odd_count = 0

# iterating each number in list
for num in range(1,100):

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)