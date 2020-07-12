# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def bin_search(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [4, 9, 5, 6, 8, 7]
r = bin_search(arr, 0)
if r != -1:
    print("Element is present at index", str(r))
else:
    print("Element is not present in array")

