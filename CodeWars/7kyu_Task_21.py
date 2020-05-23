def example_sort(arr, example_arr):
    Y = []
    for y in example_arr:
        for x in arr:
            if x == y:
                Y.append(x)
    return Y


A = example_sort([1, 2, 3, 3, 3, 4, 5], [2, 3, 4, 1, 5])
print(A)

'''
    for x in arr:
        for y in example_arr:
            while x!=y:



            arr[x]
    pass







#test.assert_equals(example_sort([1,2,3,3,3,4,5],[2,3,4,1,5]),[2,3,3,3,4,1,5])
'''
