def linearSearch(arr, target):
    for x in range(len(arr)):
        if arr[x].x == target:
            return True
    return False
