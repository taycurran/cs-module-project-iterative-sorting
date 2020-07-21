def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            return index
    else:
        return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr = sorted(arr)
    first = 0
    last = len(arr) - 1
    found = False
    while( first <= last and not found):
        mid = (first + last) // 2
        if arr[mid] == target:
            index = mid
            found = True
            return index
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if not found:
        return -1

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
arr2 = []
arr3 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
