def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


arr = [10, 20, 30, 40]
r = search(arr, 10)
if r != -1:
    print("Element is present at index", str(r))
else:
    print("Element is not present in array")
r = search(arr,0)
if r != -1:
    print("Element is present at index", str(r))
else:
    print("Element is not present in array")