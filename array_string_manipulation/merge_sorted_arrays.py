def merge_sorted_arrays(input, input2):
    # 1. Keep indicies for both arrays
    # 2. Compare both and add whichever is smallest to a result array
    # 3. Increment the index of the smaller element

    # 1.
    input_index = 0
    input2_index = 0

    result = []

    while input_index < len(input) or input2_index < len(input2):
        input_exhausted = input_index >= len(input)
        input2_exhausted = input2_index >= len(input2)

        # 2.
        if input_exhausted:
            input2_index = add_to_result(input2, input2_index, result)
        elif input2_exhausted:
            input_index = add_to_result(input, input_index, result)
        elif input[input_index] < input2[input2_index]:
            input_index = add_to_result(input, input_index, result)
        else:
            input2_index = add_to_result(input2, input2_index, result)

    
    print(result)
    
def add_to_result(input, index, result):
    # 3.
    result.append(input[index])
    index += 1

    return index

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

merge_sorted_arrays(my_list, alices_list)