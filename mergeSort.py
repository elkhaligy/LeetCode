def merge(array, leftArr, rightArr):
    i = j = k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] > rightArr [j]:
            array[k] = rightArr[j]
            j += 1
        else:
            array[k] = leftArr[i]
            i += 1
        k += 1

    while i < len(leftArr):
        array[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        array[k] = rightArr[j]
        j += 1
        k += 1


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftArr = array[:mid]
        rightArr = array[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        merge(array, leftArr, rightArr)

arr = [6,5,4,3,2,1]
mergeSort(arr)
for num in arr:
    print (num)