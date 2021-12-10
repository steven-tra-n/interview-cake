def reverse_words(input):
    # 1. Convert chars into strings, seperated by spaces
    # 2. Insert those strings into a list
    # 3. Reverse that list

    result = []
    tempString = ''

    for char in input:
        if char == ' ':
            result.append(tempString) # 2.
            tempString = ''
        else:
            tempString += char # 1.
    
    result.append(tempString)

    index = 0

    # 3.
    while index < len(result) / 2:
        placeholder = result[-1 - index]
        result[-1 - index] = result[index]
        result[index] = placeholder

        index += 1
        

    print(result)


def reverse_words_in_place(input):
    # 1. Reverse the entire input
    # 2. Reverse it again, seperated by white spaces
    # 3. Keep track of starting index 
    # 4. Iterate until a space is found
    # 5. Reverse that word

    # 1.
    reverse_characters(input, 0, len(input) - 1)

    # 3.
    start = 0

    # + 1 to cover end of string
    for i in range(len(input) + 1):
        # 4.
        if i == len(input) or input[i] == ' ':
            #  5.
            reverse_characters(input, start, i - 1)
            start = i + 1


    print(input)


def reverse_characters(input, start, end):
    while start < end:
        temp = input[end]
        input[end] = input[start]
        input[start] = temp

        start += 1
        end -= 1

input = [ 'c', 'a', 'k', 'e', ' ',
        'p', 'o', 'u', 'n', 'd', ' ',
        's', 't', 'e', 'a', 'l' ]


# reverse_words(input)
reverse_words_in_place(input)