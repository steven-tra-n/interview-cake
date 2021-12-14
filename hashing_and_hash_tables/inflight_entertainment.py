def inflight_entertainment(flight_length, movie_lengths):
    # 1. add each movie length into a dictionary
    # 2. while adding, also check to see if there are any 
    #    entries in the dictionary that match the negative

    movie_lengths_dictionary = {}
    index = 0

    # 1.
    while index < len(movie_lengths):
        movie_lengths_dictionary[index] = movie_lengths[index]

        # assumes all inputs are positive
        if flight_length - movie_lengths[index] in movie_lengths_dictionary.values():
            return True

        index += 1

    return False

flight_length = 90
movie_lengths = [30, 20, 40]

print(inflight_entertainment(flight_length, movie_lengths))