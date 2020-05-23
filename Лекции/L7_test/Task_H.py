def dot_product(N,vec1,vec2): # скалярное произведение
	
	V_res=[0]*N

	for i in range(N):
		V_res[i]=vec1[i]*vec2[i]
	
	return sum(V_res)

#print(dot_product([1,2,3],[1,2,3]))
#print(dot_product([1,2,3],[4,5,6]))