import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(225, 550)
nail_coords = gr.Point(400, 200)
velocity = gr.Point(0, 0)
acceleration = gr.Point(0, 0)





#Обьект Circle создается здесь лишь ОДИН раз
circle = gr.Circle(coords, 10)
circle.setFill('blue')
circle.draw(window)



def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point

def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point




def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


nail = gr.Circle(nail_coords, 3)
nail.setFill('black')
nail.draw(window)


def update_coords(coords, velocity):
    return add(coords, velocity)






def update_horisontal_acceleration(coords, nail_coords):
    diff = sub(coords, nail_coords)
    distance_3 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x*G/distance_3, 0)



vertical_top = gr.Point(nail_coords.x, coords.y)
vertical_bot = gr.Point(nail_coords.x, nail_coords.y+((coords.x-nail_coords.x)**2 + (coords.y-nail_coords.y)**2)**(1/2))
vertical_center = gr.Point(nail_coords.x, vertical_top.y + (vertical_bot.y - vertical_top.y)/2)






def update_vertical_acceleration(coords, vertical_center):
    diff = sub(coords, vertical_center)
    distance_4 = (diff.x ** 2 + diff.y ** 2) ** (3/2)



    G = 2000




    

    return gr.Point(0, -diff.y*G/distance_4)







while True:

	circle.move(velocity.x, velocity.y)
	velocity = update_velocity(velocity, acceleration)
	acceleration=update_horisontal_acceleration(coords, nail_coords)
	#acceleration=update_vertical_acceleration(coords, vertical_center)
	coords = update_coords(coords, velocity)

	gr.time.sleep(0.02)


