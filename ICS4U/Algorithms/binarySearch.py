def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid].x < target:
            low = mid + 1
        elif arr[mid].x > target:
            high = mid - 1
        else:
            return(True)
    return(False)
