# python3
from itertools import combinations

def Merge(arr, tmp, low, mid, high):
    i = low
    k = low
    j = mid + 1
    count = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1
            j += 1
            count += mid-i+1

    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1

    while j <= high:
        tmp[k] = arr[j]
        k += 1
        j += 1

    for var in range(low, high + 1):
        arr[var] = tmp[var]

    return count

def MergeSort(arr, tmp, low, high):
    # Base case
    if low >= high:
        return 0

    # count - record how many inversions found
    # mid - the middle point of the array
    count = 0
    mid = low + (high-low) // 2

    # Left half and Right half
    count += MergeSort(arr,tmp,low,mid)
    count += MergeSort(arr,tmp,mid+1,high)
    count += Merge(arr,tmp,low,mid,high)

    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    tmp = [0] * input_n
    print(MergeSort(elements,tmp,0,input_n-1))
