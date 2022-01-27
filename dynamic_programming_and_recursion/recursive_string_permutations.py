def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    # Break down into subproblems
    chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursion
    permutations_chars_except_last = get_permutations(chars_except_last)

    permutations = set()

    # Insert last char in each position
    for permutations_chars_except_last in permutations_chars_except_last:
        for position in range(len(chars_except_last) + 1):
            permutation = (
                permutations_chars_except_last[:position] +
                last_char +
                permutations_chars_except_last[position:]
            )

            permutations.add(permutation)

    return permutations


string = 'cats'

print(get_permutations(string))