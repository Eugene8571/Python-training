import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 400)
velocity = gr.Point(0, 0)
acceleration = gr.Point(0, 1)


#Обьект Circle создается здесь лишь ОДИН раз
circle = gr.Circle(coords, 10)
circle.setFill('blue')
circle.draw(window)







def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point

def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point



def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)










while True:
	#Метод move передвигает обьект circle  относительно его текущего положения
	circle.move(velocity.x, velocity.y)




	#отскок

	coords = update_coords(coords, velocity)
	check_coords(coords, velocity)


	velocity = update_velocity(velocity, acceleration)



	
	#print(coords)

	gr.time.sleep(0.02)





"""
SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)





    
    

    

"""