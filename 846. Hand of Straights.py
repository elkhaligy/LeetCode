from collections import defaultdict
def isNStraightHand_79testcases(hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    hand.sort()
    cnt = 0
    for i in range(n // groupSize):
        for j in range(i * groupSize, i * groupSize + groupSize - 1):
            if hand[j + 1] - hand[j] > 1:
                return False
    return True

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    hand.sort()
    freq_dict = defaultdict(int)
    for card in hand:
        freq_dict[card] += 1
    picked = []
    for i in range(n//groupSize):
        ite = groupSize
        for key, value in freq_dict.items():
            if ite != 0:
                if value != 0:
                    picked.append(key)
                    freq_dict[key] -= 1
                    ite -= 1
        if len(picked) < groupSize:
            return False
        for k in range(len(picked) - 1):
            if picked[k + 1] - picked[k] > 1:
                return False 
        picked = []
    return True

def isNStraightHand_opt(hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    
    #hand.sort()

    freq_dict = defaultdict(int)
    for card in hand:
        freq_dict[card] += 1

    freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[0]))
    #print(freq_dict)
    picked_items = []
    # Repeat the same logic on each group
    for _ in range(n // groupSize):
        picked = 0
        for key, value in freq_dict.items():
            # if value == 0:
            #     continue
            if picked != groupSize:
                if len(picked_items) > 0:
                    if key - picked_items[-1] != 1:
                        return False
                picked_items.append(key)
                freq_dict[key] -= 1
                if freq_dict[key] == 0:
                    freq_dict.pop(key)
                picked += 1
            else:
                break
        #print(picked_items)
        if len(picked_items) != groupSize:
            return False
        picked_items = []
    return True


def isNStraightHand_78testcases(hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    
    hand.sort()

    freq_dict = defaultdict(int)
    for card in hand:
        freq_dict[card] += 1
    
    for i in range(0, n - 1):
        card = hand[i]
        if card == -1:
            continue
        if card + 1 in freq_dict and freq_dict[card + 1] > 0:
            freq_dict[card + 1] -= 1
            for k in range(i + 1, len(hand)):
                if hand[k] == card + 1:
                    hand[k] = -1
                    break
        else:
            return False
    return True

def findCons(hand, groupSize, i):
    next_ele = hand[i] + 1
    hand[i] = -1
    current_picked = 1
    i += 1
    while i < len(hand) and current_picked < groupSize:
        if hand[i] == next_ele:
            next_ele = hand[i] + 1
            hand[i] = -1
            current_picked += 1
        i += 1
    return current_picked == groupSize


def isNStraightHand_try2(hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    if groupSize == 1:
        return True
    hand.sort()

    for i in range(n):
        if hand[i] == -1:
            continue
        
        if not findCons(hand, groupSize, i):
            return False
        
    return True





print(isNStraightHand_try2( [1,1,2,2,3,3], groupSize = 3))