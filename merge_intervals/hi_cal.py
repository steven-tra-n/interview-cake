def merge_range(meetings):
    # 1. Sort meetings
    # 2. Append first meeting
    # 3. Compare meeting end time with next meeting start time
    # 4. Edge cases?
     
    # 4.
    if len(meetings) == 1:
        return meetings

    result = []

    sorted_meetings = sorted(meetings)

    result.append(sorted_meetings[0])

    print(result)

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
merge_range(meetings)