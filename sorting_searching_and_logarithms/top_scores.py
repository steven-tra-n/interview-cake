def top_scores(scores, max_possible_score):
    # 1. Loop once through the array, put values into max heap
    # 2. Array will be sorted after first run through
    # 3. What if we are not allowed to use a heap?
    # 4. Make empty array from 1 to maxiumum score
    # 5. Indicies will represent the score. Values will keep count
    # 6. Loop through once and update array with counts
    # 7. Loop backwards through array and append them to a resulting array

    # 4.
    score_counts = [0] * (max_possible_score + 1)
    result = []

    # 6.
    for score in scores:
        score_counts[score] += 1

    # 7.
    for i in range(len(score_counts) -1, -1, -1):
        count = score_counts[i]

        for j in range(count):
            result.append(i)

    print(result)

scores = [10, 90, 20, 20, 90, 80, 90, 50]
top_scores(scores, 90)