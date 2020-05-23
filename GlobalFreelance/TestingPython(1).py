def figure_in_num(N, i):
	if len(str(N))<i+1:
		return 0
	return int(str(N)[i])

print(figure_in_num(123, 2))