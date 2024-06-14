from collections import Counter
def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    arr1.sort()
    arr1_frequency_dict = Counter(arr1)
    sorted_result = []
    
    for number in arr2:
        while arr1_frequency_dict[number]:
            sorted_result.append(number)
            arr1_frequency_dict[number] -= 1
    
    for number, frequency in arr1_frequency_dict.items():
        if frequency > 0:
            while arr1_frequency_dict[number]:
                sorted_result.append(number)
                arr1_frequency_dict[number] -= 1
    
    return sorted_result    


print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))