def find_even_index(arr):
    if sum(arr[1:]) == 0:
        return 0
    if sum(arr[:-1]) == 0:
        return len(arr) - 1
    for i in range(1, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

print(find_even_index([1,2,3,4,3,2,1]))