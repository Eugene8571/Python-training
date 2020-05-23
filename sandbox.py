def snail(array):
    if array == [[]]:
        return []
    
    res = []
    for i in range(len(array[0]) - 1):
        res += array[i]
        for j 



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array) == [1,2,3,6,9,8,7,4,5])
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array) == [1,2,3,4,5,6,7,8,9])



