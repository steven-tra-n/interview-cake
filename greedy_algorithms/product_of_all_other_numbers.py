def product_of_all_other_numbers(numbers):
    # # 1. Multiply all numbers leading to index
    # # 2. Multiply all numbers after index
    # result = []

    # for index, number in enumerate(numbers):
    #     current_product = 1

    #     print('index:', index)

    #     for number2 in numbers[:index]:
    #         current_product *= number2

    #     for number3 in numbers[index:]:
    #         current_product *= number3

    #     result.append(current_product)

    # print(result)

    # End brute force solution

    # # 1. Create an array storing the product of numbers before an occuring index
    # # 2. Repeat for numbers occuring after index

    # product_before_index = []
    # product_after_index = []
    # result = []

    # # 1.
    # product_before_index = populate_array(product_before_index, numbers)

    # # 2.
    # product_after_index = populate_array(product_after_index, reversed(numbers))

    # product_after_index.reverse()

    # for i in range(len(numbers)):
    #     result.append(product_before_index[i] * product_after_index[i])

    # print(result)

    # End two list solution

    # 1. Create an array storing all products before the index
    # 2. Traverse the numbers array in reverse and multiply it with the array from 1.

    if len(numbers) < 2:
        raise IndexError('Need at least 2 numbers')

    result = [None] * len(numbers)
    product_so_far = 1

    # 1.
    for i in range(len(numbers)):
        result[i] = product_so_far
        product_so_far *= numbers[i]

    # Reset
    product_so_far = 1

    # 2.
    for i in range(len(numbers) - 1, -1, -1):
        result[i] = product_so_far * result[i]
        product_so_far *= numbers[i]

    print(result)



# def populate_array(array, numbers):
#     previous_number = 1

#     for index, number in enumerate(numbers):
#         if index == 0:
#             array.append(previous_number)
#         else:
#             array.append(array[index - 1] * previous_number)

#         previous_number = number

#     return array

numbers = [3, 1, 2, 5, 6, 4]

product_of_all_other_numbers(numbers)