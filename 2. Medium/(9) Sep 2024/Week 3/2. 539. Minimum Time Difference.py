def findMinDifference(timePoints: list[str]) -> int:
    minutes = convert_to_minutes(timePoints)
    minutes.sort()
    minimum = get_min(minutes)
    return minimum

def get_min_bruteforce(minutes: list[int]):
    min_til_now = float('inf')

    for i in range(len(minutes) - 1):
        for j in range(i + 1, len(minutes)):
            min_til_now = min(min_til_now, minutes[j] - minutes[i], abs((1440 - minutes[j]) + minutes[i]))
    
    return min_til_now

def get_min(minutes: list[int]):
    min_til_now = float('inf')

    for i in range(1, len(minutes)):
        min_til_now = min(min_til_now, minutes[i] - minutes[i - 1], abs(1440 - minutes[i] + minutes[i - 1]))
    
    min_til_now = min(min_til_now, 1440 - minutes[-1] + minutes[0])
    
    return min_til_now

def convert_to_minutes(timePoints: list[int]) -> list[int]:
    minutes = []

    for time in timePoints:
        total_minutes = 0
        total_minutes += int(time[:2]) * 60
        total_minutes += int(time[3:])
        minutes.append(total_minutes)
    
    return minutes

#print(findMinDifference(timePoints = ["01:01","02:01","03:00"]))
print(findMinDifference(timePoints =["01:01","02:01","03:00"]

))
