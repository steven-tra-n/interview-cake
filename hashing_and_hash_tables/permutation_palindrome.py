def permutation_palindrome(input):
    # 1. store all chars in a dictionary
    # 2. Only one char max is allowed to be odd numbered

    # charDictionary = {}
    # odd_number_counter = 0

    # # 1.
    # for char in input:
    #     # booleans can be used instead of actual char count to avoid interger overflow
    #     charDictionary[char] = charDictionary.get(char, 0) + 1

    # # 2.
    # for entry in charDictionary.items():
    #     if entry[1] % 2 == 1:
    #         odd_number_counter += 1


    # print(odd_number_counter == 1)

    # end dictionary solution

    # 1. loop through input
    # 2. if char is inside set, remove it
    # 3. if not, add it
    # 4. only one char max should be odd numbered, return the size of the set

    charSet = set()

    # 1.
    for char in input:
        if char in charSet: # 2.
            charSet.remove(char)
        else: # 3.
            charSet.add(char)

    # 4.
    print(len(charSet) <= 1)

input = 'cccc'

permutation_palindrome(input)