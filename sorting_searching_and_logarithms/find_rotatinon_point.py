def find_rotation_point(words):
    # 1. We can utilize the fact that a is mostly < b
    # 2. The list is partly sorted, so we can use a modified binary search
    # 3. If the first word is < mid word, the rotation point is somewhere in second half
    # 4. Vice versa
    # 5. Rotation point will be found when left and right collide
    # 6. If list is already sorted?

    # left = 0
    # right = len(words) - 1
    # first_word = words[0]
    # first_mid_word = words[(left + right) // 2]

    # # 6.
    # # if(first_word <= first_mid_word):
    # #     return 0
    
    # while left < right:
    #     mid = (right + left) // 2

    #     # 3.
    #     if words[mid] >= first_word:
    #         left = mid
    #     else: # 4.
    #         right = mid

    #     # 5.
    #     if left + 1 == right:
    #         return right

    # End interview cake solution

    # 1. Utilize a modified binary search
    # 2. When the word in the middle is less than the first word, the rotated point is in the second half
    # 3. Else, rotated part is in the first half
    # 4. Array is not even rotated

    left = 0
    right = len(words) - 1

    while left < right:
        mid = left + (right - left) // 2

        if words[mid] < words[left]: # 2.
            right = mid
        else: # 3.
            left = mid + 1

    # 4.
    if right == len(words) - 1:
        return 0
    else: 
        return right

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(find_rotation_point(words))