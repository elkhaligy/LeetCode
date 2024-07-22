def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    combined = zip(names, heights)
    sorted_combined = sorted(combined, key= lambda a: a[1], reverse= True)

    result = []
    for tup in sorted_combined:
        result.append(tup[0])

    return result

def sortPeople_sol2(names: list[str], heights: list[int]) -> list[str]:
    dct = {}
    for i in range(len(names)):
        dct[heights[i]] = names[i]

    sorted_heights = sorted(heights, reverse=True)

    result = [dct[height] for height in sorted_heights]
        
    return result
print(sortPeople_sol2(names = ["Mary","John","Emma"], heights = [180,165,170]))