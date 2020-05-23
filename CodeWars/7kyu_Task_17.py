def solution(nums):
    if type(nums) is list:
    	nums.sort()
    	return nums
    return [] 
    



A=solution([1,2,10,5])
print(A)

#print(type([1,2,10,5]))