def merge_meetings(meetings):
    # 1. Sort meetings
    # 2. Append first meeting
    # 3. Loop through and compare meeting end time with previous meeting start time
    # 4. If the meeting start time is less than or equal to previous, they can be merged
    # 5. Edge cases?
     
    # 4.
    if len(meetings) == 1:
        return meetings

    result = []

    # 1.
    sorted_meetings = sorted(meetings)

    # 2.
    result.append(sorted_meetings[0])

    # 3.
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        previous_meeting_start, previous_meeting_end = result[-1]

        if current_meeting_start <= previous_meeting_end:
            result[-1] = (previous_meeting_start, max(previous_meeting_end, current_meeting_end))
        else:
            result.append((current_meeting_start, current_meeting_end))


    print(result)

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]

merge_meetings(meetings)