def survivedRobotsHealths(positions: list[int], healths: list[int], directions: str) -> list[int]:
        # It is better to use deque
        stack = []
        # Start making tuple (position, health, direction) sorted from lowest pos to highest
        list_of_tuples = list(zip(positions, healths, directions))
        list_of_tuples.sort(key= lambda a: a[0])

        def stack_checker(stack):
            while len(stack) >= 2 and stack[-1][2] == 'L' and stack[-2][2] == 'R':
                popped_1 = stack.pop()
                popped_2 = stack.pop()
                survivor = popped_1 if popped_1[1] >= popped_2[1] else popped_2
                if not popped_1[1] == popped_2[1]:            
                    stack.append((survivor[0], survivor[1] - 1, survivor[2]))

        # Iterate through sorted posistion and apply stack algorithm
        for tup in list_of_tuples:
            stack_checker(stack)
            # Checking if the directions are not the same, in this case a collision must happen
            if stack and (tup[2] == 'L' and stack[-1][2] == 'R'):
                survivor = tup if tup[1] >= stack[-1][1] else stack[-1]
                # Equal health but different robots pop both two
                if survivor[1] == stack[-1][1] and survivor != stack[-1]:
                    stack.pop()
                # Not Equal health, pop the loser push the winner
                elif survivor != stack[-1][1]:
                    stack.pop()
                    stack.append((survivor[0], survivor[1] - 1, survivor[2]))
            else:
                stack.append(tup)
        #print(list_of_tuples, stack)

        stack_checker(stack)
        if not stack:
            return []

        winners_positions = set()
        pos_hel_dict = {}
        for tup in stack:
            winners_positions.add(tup[0])
            pos_hel_dict[tup[0]] = tup[1]
        
        ans = []
        for pos in positions:
            if pos in winners_positions:
                ans.append(pos_hel_dict[pos])
        return ans

# Editorial Solution: More clean as they're using indices directly
def survivedRobotsHealths_sol2(positions: list[int], healths: list[int], directions: str) -> list[int]:
    n = len(positions)
    indices = list(range(n))
    stack = []

    
    indices.sort(key= lambda x: positions[x])

    for index in indices:
        if directions[index] == 'R':
            stack.append(index)
        else:
            while stack and healths[index] > 0:
                top_index = stack.pop()
                if healths[top_index] > healths[index]:
                    healths[top_index] -= 1
                    healths[index] = 0
                    stack.append(top_index)
                elif healths[top_index] < healths[index]:
                    healths[index] -= 1
                    healths[top_index] = 0
                else:
                    healths[index] = 0
                    healths[top_index] = 0

    ans = []
    for index in range(n):
        if healths[index] > 0:
            ans.append(healths[index])

    return ans
                 

print(survivedRobotsHealths_sol2(positions =[29,7,31,42], healths = [19,24,26,10], directions = "RRLR"))