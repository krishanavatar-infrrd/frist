def margeSort(arr, low, high):
    if low < high:
        mid = int((low + high)/2)
        margeSort(arr, low, mid)
        margeSort(arr, mid + 1, high)
        marger(arr, low, high, mid)


def marger(arr, low, high, mid):
    x = low
    y = mid + 1

    na = []
    while x <= mid and y <=high:
        if arr[x] <arr[y]:
            na.append(arr[x])
            x += 1
        else:
            na.append(arr[y])
            y += 1
    while x <= mid:
        na.append(arr[x])
        x += 1
    while y <= high:
        na.append(arr[y])
        y += 1



    arr[low:high+1]=na
    '''
    inx = 0
    for x in range(low ,high+1):
        arr[x]=na[inx]
        inx+=1'''


ls = [2, 5, 87, 3, 2, 5, 86, 43, 34]
print(ls)
le = len(ls) - 1


margeSort(ls, 0, le)
print(ls)
