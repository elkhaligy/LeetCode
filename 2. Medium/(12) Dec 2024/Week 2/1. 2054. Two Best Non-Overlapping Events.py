def maxTwoEvents(events: list[list[int]]) -> int:
    times = []
    for event in events:
        times.append([event[0], 1, event[2]])
        times.append([event[1] + 1, 0, event[2]])
    times.sort()

    ans = 0
    maxVal = 0

    for time in times:
        if time[1]:
            ans = max(ans, time[2] + maxVal)
        else:
            maxVal = max(maxVal, time[2])

    return ans



print(maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]]))
