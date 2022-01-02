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

    numbers.sort()
    previous_number = numbers[0]

    for number in numbers[1:]:
        if number == previous_number:
            return number

        previous_number = number

    print(numbers)

    # End solution with sort. O(n) time and O(1) space

numbers = [1, 4, 6, 2, 5, 3, 3]

print(find_repeat(numbers))