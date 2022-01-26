def find_repeat_beast(numbers):
    # 1. Treat the array as a linked list. The value of the node points the the valueth number on the array
    # 2. Use a fast and slow approach
    # 3. Find how long the cycle is first
    # 4. Reset head
    # 5. Reinitiate fast to be the length of the cycle ahead
    # 6. Advance both pointers by one
    # 7. Their intersection will be where the cycle starts

    slow = numbers[len(numbers) - 1]
    fast = slow
    cycle_counter = 0
    found_cycle = False

    while True:
        # 2.
        slow = numbers[slow - 1]
        fast = numbers[fast - 1]
        fast = numbers[fast - 1]

        # 3.
        if slow == fast:
            if cycle_counter > 0:
                break
            else:
                found_cycle = True

        if found_cycle:
            cycle_counter += 1

    # 4.
    slow = numbers[len(numbers) - 1]
    fast = slow

    for i in range(cycle_counter):
        # 5.
        fast = numbers[fast - 1] 

    while True:
        if slow == fast:
            # 7.
            return slow

        # 6.
        slow = numbers[slow - 1]
        fast = numbers[fast - 1]
        

numbers = [4, 3, 1, 1, 4]

print(find_repeat_beast(numbers))