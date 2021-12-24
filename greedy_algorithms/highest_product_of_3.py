import heapq

def highest_product_of_3(numbers):
    # 1. Initialize a max heap with the first 3 numbers
    # 2. Get their product and store it in a variable
    # 3. Iterate through the array and try to find greater products
    # 4. Is the new product with 4 numbers greater than the max if we divide by the smallest number?

    # min_heap = []
    # heapq.heapify(min_heap)
    # max_product = 1
    # current_product = 0

    # # 1.
    # for number in numbers[:3]:
    #     heapq.heappush(min_heap, number)

    #     # 2.
    #     max_product *= number

    # for number in numbers[3:]:
    #     min_number = heapq.heappop(min_heap)
    #     current_product = max_product * number
    #     current_product_after_division = current_product / min_number

    #     if current_product_after_division > max_product:
    #         max_product = current_product_after_division
    #         heapq.heappush(min_heap, number)
    #     else:
    #         heapq.heappush(min_heap, min_number)

    # print(max_product)

    # End heap solution

    # 1. Keep track of the largest and smallest (for negatives) products of 2
    # 2. Start off with the first 2, then iterate through the rest of the array
    # 3. Start iterating with the third element. Multiply it with the highest 2 and lowest 2
    # 4. See if we have a new highest 2 or lowest 2
    # 5. See if we have a new highest or lowest

    if(len(numbers) < 3):
        raise ValueError('Need at least 3 numbers.')

    # 2.
    highest = max(numbers[0], numbers[1])
    lowest = min(numbers[0], numbers[1])
    highest_product_of_2 = numbers[0] * numbers[1]
    lowest_product_of_2 = numbers[0] * numbers[1]

    highest_product_of_3 = numbers[0] * numbers[1] * numbers[2]

    # 3.
    for number in numbers[3:]:
        highest_product_of_3 = max(highest_product_of_3,
                                    highest_product_of_2 * number,
                                    lowest_product_of_2 * number)

        # 4.
        highest_product_of_2 = max(highest_product_of_2, 
                                    highest * number,
                                    lowest * number)

        lowest_product_of_2 = min(lowest_product_of_2, 
                                    lowest * number,
                                    highest * number)

        # 5.
        highest = max(highest, number)
        lowest = min(lowest, number)

    print(highest_product_of_3)


numbers = [1, 6, 3, 4, 2]

highest_product_of_3(numbers)