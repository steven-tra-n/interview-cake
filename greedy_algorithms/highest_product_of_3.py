import heapq

def highest_product_of_3(numbers):
    # 1. Initialize a max heap with the first 3 numbers
    # 2. Get their product and store it in a variable
    # 3. Iterate through the array and try to find greater products
    # 4. Is the new product with 4 numbers greater than the max if we divide by the smallest number?

    min_heap = []
    heapq.heapify(min_heap)
    max_product = 1
    current_product = 0

    # 1.
    for number in numbers[:3]:
        heapq.heappush(min_heap, number)

        # 2.
        max_product *= number

    for number in numbers[3:]:
        min_number = heapq.heappop(min_heap)
        current_product = max_product * number
        current_product_after_division = current_product / min_number

        if current_product_after_division > max_product:
            max_product = current_product_after_division
            heapq.heappush(min_heap, number)
        else:
            heapq.heappush(min_heap, min_number)

    print(max_product)


numbers = [-10,-10,1,3,2]

highest_product_of_3(numbers)