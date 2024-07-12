def passThePillow_simulation(n: int, time: int) -> int:
    curr_person = 1
    reverse_flag = False
    while time:
        time -= 1
        if reverse_flag:
            curr_person -= 1
        else:
            curr_person += 1
        if curr_person == n:
            reverse_flag = True
        if curr_person == 1:
            reverse_flag = False
    return curr_person
         
def passThePillow_math(n: int, time: int) -> int:
    quot = time // (n - 1)
    rem = time % (n - 1)
    if quot % 2 == 0:
        return 1 + rem
    else:
        return n - rem
print(passThePillow_simulation(n = 4, time = 5))
