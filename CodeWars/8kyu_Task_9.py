def divisible_by(numbers, divisor):
	A=[]
	for i in numbers:
		if i%divisor==0:
			A.append(i)
	return(A)

R=divisible_by([1,2,3,4,5,6], 2)
print(R)


'''
Test.describe("Fixed tests")
Test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
Test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
Test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
Test.assert_equals(divisible_by([0], 4), [0])
Test.assert_equals(divisible_by([1,3,5], 2), [])
'''