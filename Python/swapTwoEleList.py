def swapEle(arr, p1, p2):
    n=len(arr)
    if (p1 and p2) <= n:
        arr[p1-1], arr[p2-1] = arr[p2-1], arr[p1-1]
    else:
        print('positions must be under size of list- ',n)
    return arr

arr = list(map(int, input('list: ').split()))
p1 = int(input('pos1: '))
p2 = int(input('pos2: '))
print(swapEle(arr, p1, p2))