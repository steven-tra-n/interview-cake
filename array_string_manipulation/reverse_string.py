def reverse_string(input):
    # 1. Loop until the middle of the list
    # 2. Swap first and last elements

    index = 0

    while index < len(input) / 2:
        temp = input[-1 - index]
        input[-1 - index] = input[index]
        input[index] = temp

        index += 1

    print(input)

input = ["H", "e", "l", "l", "o", "!"]

reverse_string(input)