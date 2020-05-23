def my_languages(results):
	'''выборка >=60
	'''
	L=[]
	for x in results:
		if results.get(x) >= 60:
			L.append(x)


	#сортировка. пузырьки

	for i in range(len(L)):


		for x in range(len(L)-1):

			if results.get(L[x]) < results.get(L[x+1]):
				print(L, '!')
				L[x], L[x+1] = L[x+1], L[x]


	return(L)





A=my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71})
print(A)

#sort_transform([82, 98, 72, 71, 71, 72, 62, 67, 68, 115, 117, 112, 122, 121, 93])
# ("Rby]->Cyz-zyC>->Cyz")