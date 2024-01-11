# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [(x ** 2) for x in numbers]

# print(squared_numbers)

# Challenge Two
#
# # List_of_ints = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
# list_of_strings = input().split(',')
# numbers = [int(x) for x in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)


# Challenge Three
# Difficulty: Hard

# Create a list called "Result"
# Contains [numbers] that are in both files1 and 2
# Output should be list of integers

with open("file1.txt", 'r') as one:
    one_list = [int(x) for x in one.readlines()]
    print(one_list)

with open("file2.txt", 'r') as two:
    second_list = [int(x) for x in two.readlines()]
    print(second_list)


merge = [x for x in one_list if (x in second_list)]
print(merge)

