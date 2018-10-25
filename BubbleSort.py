def bubbleSort(arr):
    for x in range(len(arr) - 1):
        for j in range(len(arr) - 1 - x):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


def selectionSort(arr):
    for i in range(len(arr)):
        inx = i
        for j in range(i + 1, len(arr)):
            if arr[inx] > arr[j]:
                inx = j
        if inx != i:
            t = arr[i]
            arr[i] = arr[inx]
            arr[inx] = t


def insertionSort(arr):
    for i in range(1,len( arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [1, 2, 34, 2, 34, 6, 7, 43, 323, 54, 6, 7, 8, 54]
print(arr)
insertionSort(arr)
print(arr)
