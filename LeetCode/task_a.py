def twoSum(nums, target):
    for i in range(len(nums)-1):
        print(i)
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twoSum([7,11,15,2], 9))