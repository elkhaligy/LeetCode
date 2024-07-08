def findTheWinner_simulation(n: int, k: int) -> int:
    friends = [i + 1 for i in range(n)]

    pop_index = 0
    while len(friends) > 1:
        pop_index = (pop_index + (k - 1)) % len(friends) 
        friends.pop(pop_index)
    
    return friends[0]

print(findTheWinner_simulation(n = 5, k = 2))
