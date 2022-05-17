def insertionSort(arr):
    newList = arr

    for i in range(1, len(newList)):
        temp = arr[i].x
        newKey = i - 1

        while newKey >= 0 and temp < newList[newKey].x:
            newList[newKey + 1].x = newList[newKey].x
            newKey -= 1
        newList[newKey + 1].x = temp
    return newList
