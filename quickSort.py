def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = -1

    for j in range(high):
        if array[j] < pivot:
            i = i + 1
            swap(array, j, i)
    
    swap(array, i+1, high)
    return i + 1

def swap(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

def main():
    array = [2,4,1,0,3]
    print(array)
    quickSort(array,0,4)
    print(array)

if __name__ == "__main__":
    main()
