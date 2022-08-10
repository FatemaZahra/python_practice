import sys
# def duplicate_count(text):
#     count = 0
#     dict = {}
#     lower_text = text.lower()
#     for alpha in range(0, len(lower_text)):
#         dict[lower_text[alpha]] = 0
#
#     for key in dict:
#         for i in range(0, len(lower_text)):
#             if (key == lower_text[i]):
#                 dict[key] = dict[key] + 1
#
#     for key in dict:
#         if (dict[key] > 1):
#             count = count + 1
#
#     return count

def odd_even_counter(number):
    list = [0,0]
    for i in range(1,number+1):
        if i % 2 == 0:
            list[0] +=i
        else:
            list[1] +=i
    return list

print(odd_even_counter(90))

def largest_number(list):
    return max(list)

print(largest_number([1,2,34,5]))

def find_smallest_interval(numbers):
    length = len(numbers)
    numbers = sorted(numbers)

    interval_diff = sys.maxsize

    for num in range(length-1):
        if numbers[num+1] - numbers[num] < interval_diff:
            interval_diff = numbers[num+1] - numbers[num]

    return interval_diff

print(find_smallest_interval([2,5.3,5,6,9]))
