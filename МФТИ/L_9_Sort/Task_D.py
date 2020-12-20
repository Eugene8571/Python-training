'''
def inflation(price,delta,m):
	money=0
	dey=1
	money+=price
	while dey<m*7:
		price=price+delta
		money+=price
		dey+=1

	return money

print(inflation(10,1,1))
'''

def inflation():
	A=[int(i) for i in input().split(' ')]
	price=A[0]
	delta=A[1]
	m=A[2]
	money=0
	dey=1
	money+=price
	while dey<m*7:
		price=price+delta
		money+=price
		dey+=1

	return money

print(inflation())

