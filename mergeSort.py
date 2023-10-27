def quickSort(array):
    if len(array) == 1:
        return

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    quickSort(left)
    quickSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    
    while i < len(left):
        array[k] = left[i]
        k = k + 1
        i = i + 1
    
    while j < len(right):
        array[k] = right[j]
        k = k + 1
        j = j + 1


def printArray(array):
    for value in array:
        print(value, end= " ")


if __name__ == "__main__":
    array = [2,4,0,1,5,3]
    # printArray(array)
    quickSort(array)
    printArray(array)