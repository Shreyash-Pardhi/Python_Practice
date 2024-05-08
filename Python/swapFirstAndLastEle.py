def swapFirstAndLast(arr):
    arr[0], arr[n-1] = arr[n-1], arr[0]
    return arr

arr = list(map(int, input().split()))
n=len(arr)
print(swapFirstAndLast(arr))
