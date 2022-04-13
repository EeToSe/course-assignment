# python3
def binary_search(keys,query):
    low = 0
    high = len(keys) -1
    found = False
    index = -1
    while(low<=high and not found):
        mid = (low + high) // 2
        if query == keys[mid]:
            found = True
            index = mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return index


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
