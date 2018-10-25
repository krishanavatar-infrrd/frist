def quickSort(arr, low, high):
    if low < high:
        x = partion(arr, low, high)
        quickSort(arr, low, x - 1)
        quickSort(arr, x + 1, high)


def partion(arr, low, high):
    pviot = arr[low]
    i = low + 1
    j = high
    while i < j:
        while i < j and arr[i] < pviot:
            i += 1
        while j>=i and arr[j] > pviot:
            j -= 1
        if i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

    arr[low] = arr[j]
    arr[j] = pviot
    return j


ls = [2, 5, 87, 3, 2, 5, 86, 43, 34]
print(ls)
le = len(ls) - 1

quickSort(ls, 0, le)
print(ls)
