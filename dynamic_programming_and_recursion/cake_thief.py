def cake_thief(capacity, cakes):
    # 1. Loop through capacity, bottom up
    # 2. Have a variable to store maximum for 1.
    # 3. In each loop, also loop through cakes
    # 4. Only check if current cake fits in the knapsack
    # 5. Check value if bigger cake would yield higher gain
    # 6. Compare to current max
    # 7. Assign max
    # 8. Edge cases

    maximum_per_capacity = [0] * (capacity + 1)

    # 1.
    for current_capcity in range(capacity + 1):
        # 2.
        current_max_value = 0

        # 3.
        for weight, worth in cakes:
            # 8.
            if weight == 0 and worth != 0:
                return float('inf')

            # 4.
            if weight <= current_capcity:
                # 5.
                take_bigger_cake = worth + maximum_per_capacity[current_capcity - weight]
                # 6.
                current_max_value = max(current_max_value, take_bigger_cake)

        # 7.
        maximum_per_capacity[current_capcity] = current_max_value

    print(maximum_per_capacity[capacity])

capacity = 3
cakes = [(1, 30), (2, 50)]

cake_thief(capacity, cakes)