from collections import defaultdict
def countCompleteDayPairs(hours: list[int]) -> int:
    dct = defaultdict(int)
    cnt = 0
    
    for index, hour in enumerate(hours):
        remainder = hours[index] % 24
        needed_remainder = (24 - remainder) % 24

        if needed_remainder in dct:
            cnt += dct[needed_remainder]
            
        dct[remainder] += 1
    return cnt

print(countCompleteDayPairs(hours = [12,12,30,24,24]))