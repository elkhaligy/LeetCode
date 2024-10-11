def smallestChair_bruteforce(times: list[list[int]], targetFriend: int) -> int:
    n = len(times)
    sorted_times = sorted(times, key = lambda tup: tup[0])
    chairs = [0] * n

    for time in sorted_times:
        for i in range(n):
            if chairs[i] <= time[0]:
                chairs[i] = time[1]
                if time == times[targetFriend]:
                    return i
                break

    return 0

def smallestChair_optmizied(times: list[list[int]], targetFriend: int) -> int:
    return 0