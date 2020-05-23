def flatten(array):
    A = []
    for x in array:
        A.extend(x)
    return (A)


def sort_arrey(A):
    A = 2


def flatten_and_sort(array):
    A = flatten(array)
    A.sort()
    return (A)


f = flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])
print(f)

