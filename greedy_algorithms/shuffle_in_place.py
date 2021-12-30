import random

def shuffle_in_place(numbers):
    # 1. Start from the first index
    # 2. Swap that with the 'random' index
    # 3. Swap the random index with the ith index

    for i in range(len(numbers)):
        placeholder = numbers[i]
        randomIndex = random.randint(i, len(numbers) - 1)

        numbers[i] = numbers[randomIndex]
        numbers[randomIndex] = placeholder
    
    print(numbers)

numbers = [1, 2, 3, 4, 5, 6]

shuffle_in_place(numbers)