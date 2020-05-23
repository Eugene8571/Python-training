import turtle as t
t.speed(8)



start_X=-500
start_Y=200
t.penup()
t.goto(start_X, start_Y)
t.pendown()

def kar(l, n):
	if n==0:

		pass
		

	elif n==1:

		t.forward(l)


	elif n==2:

		t.forward(l)

		t.penup()
		t.left(180)
		t.forward(l)
		t.left(90)
		t.forward(10)
		t.left(90)
		t.pendown()

		
		t.forward(l/3)
		t.penup()
		t.forward(l/3)
		t.pendown()
		t.forward(l/3)



		t.penup()
		t.left(90)
		t.forward(10)
		t.right(90)
		t.pendown()










	elif n>2:

		t.forward(l)

		t.penup()
		t.left(180)
		t.forward(l)
		t.left(90)
		t.forward(10)
		t.left(90)
		t.pendown()


		
		kar(l/3, n-1)





		t.penup()
		t.forward(l/3)
		t.pendown()

		kar(l/3, n-1)

		t.penup()
		t.left(90)
		t.forward(10)
		t.right(90)
		t.pendown()




kar(500, 7)


'''











		for x in range(1, n):
			t.penup()
			t.goto(start_X, start_Y-10*x)
			t.pendown()







for x in range(n):
	t.penup()
	t.goto(start_X, start_Y-10*x)
	t.pendown()
	kao(l, n)
	l/=3
	pass






		t.penup()
		t.forward(l)
		t.pendown()
		
		


		
		l/=3

		kao(l, n)
		kao(l, n)
		
	elif n==2:





		for x in range(1, n):
			kao(l, x)
			t.penup()
			t.goto(start_X, start_Y-10*x)
			t.pendown()
			l/=3





kao(500, 0)

		

		t.goto(start_X, start_Y+10*(n+1))

		l/=3


		t.forward(l)
		t.penup()
		t.forward(l)
		t.pendown()
		t.forward(l)

	elif n==2:
		for x in range(n):
		
			kao(l, x)
			t.penup()
			t.goto(start_X, start_Y+10*x)
			t.pendown()






	

'''