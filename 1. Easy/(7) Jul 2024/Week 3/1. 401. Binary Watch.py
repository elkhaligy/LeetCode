def readBinaryWatch(turnedOn: int) -> list[str]:
    watch = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
    result = []

    def recursive(curr_index: int, hours: int, mins: int, trials: int):
        if hours >= 12 or mins >= 60:
            return
        
        if trials == 0:
            result.append(f"{hours}:{str(0) * (mins < 10)}{mins}")
            return
        
        if curr_index < len(watch):
            if curr_index <= 3:
                recursive(curr_index + 1, hours + watch[curr_index], mins, trials - 1)
            else:
                recursive(curr_index + 1, hours, mins + watch[curr_index], trials - 1)
            recursive(curr_index + 1, hours, mins, trials)

    recursive(0, 0, 0, turnedOn)

    return result


print(readBinaryWatch(1))
