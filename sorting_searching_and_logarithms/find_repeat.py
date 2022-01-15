def find_repeat(numbers):
    # 1. Add each entry into a set
    # 2. If it already exists, return that element

    # number_set = set()

    # for number in numbers:
    #     if number in number_set:
    #         return number
        
    #     number_set.add(number)

    # return number_set

    # End solution with set. O(n) time and O(n) space
    # Can we do better than O(n) space?

    # 1. Sort array first
    # 2. Use a variable to store the current element
    # 3. Check if the element in i + 1 is equal to it

    # numbers.sort()
    # previous_number = numbers[0]

    # for number in numbers[1:]:
    #     if number == previous_number:
    #         return number

    #     previous_number = number

    # print(numbers)

    # End solution with sort. O(n) time and O(1) space
    # This modifies input though. Can we do this without modifying the input?

    # 1. Divide the list in half, seperating the list into 1 to n/2 and n/2 + 1 to n
    # 2. Find number of possible distinct numbers for left half
    # 3. If that number is greater than the left half, then the duplicate lives in the right half
    # 4. Repeat

    left_floor = 1
    right_ceiling = len(numbers) - 1


    while left_floor < right_ceiling:
        # 1.
        mid = left_floor + (right_ceiling - left_floor) // 2
        left_ceiling = mid

        left_half_count = 0

        for number in numbers:
            # 2.
            if number >= left_floor and number <= left_ceiling:
                left_half_count += 1

        possible_distinct_left_numbers = left_ceiling - left_floor + 1

        # 3.
        if left_half_count > possible_distinct_left_numbers:
                right_ceiling = mid
        else:
            left_floor = mid + 1

    return left_floor

# numbers = [1, 4, 6, 2, 5, 3, 4]
numbers = [1, 2, 3, 4, 5, 5, 6]

print(find_repeat(numbers))