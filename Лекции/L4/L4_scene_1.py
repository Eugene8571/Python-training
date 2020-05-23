import graphics as gr

window = gr.GraphWin("Scene 1", 1000, 1000)


def sun_right(x, y, size):
    
    sun_circle=gr.Circle(gr.Point(x, y), size)
    sun_circle.setFill('yellow')
    sun_circle.setOutline('yellow')
    sun_circle.draw(window)
    
    radians1=gr.Line(gr.Point(x, y+100), gr.Point(x, y+190))
    radians1.setOutline('yellow')
    radians1.setWidth(15)
    radians1.draw(window)

    radians2=gr.Line(gr.Point(x-70, y+73), gr.Point(x-140, y+137))
    radians2.setOutline('yellow')
    radians2.setWidth(15)
    radians2.draw(window)

    radians3=gr.Line(gr.Point(x-100, y+11), gr.Point(x-200, y+40))
    radians3.setOutline('yellow')
    radians3.setWidth(15)
    radians3.draw(window)

    radians4=gr.Line(gr.Point(x-94, y-52), gr.Point(x-200, y-104))
    radians4.setOutline('yellow')
    radians4.setWidth(15)
    radians4.draw(window)

def cloud_part(x, y, size):
    cloud_part_0=gr.Circle(gr.Point(x, y), size)
    cloud_part_0.setFill('gray')
    cloud_part_0.draw(window)
  
    
def cloud(x, y, size):
    s=size
    cloud_part(x, y, s)
    cloud_part(x+0.5*s, y+1*s, s)
    cloud_part(x+1.1*s, y, 1.2*s)
    cloud_part(x+2*s, y, s)
    cloud_part(x+1.5*s, y+0.85*s, s)
    
    

    
sun_right(800, 200, 75)
cloud(500, 150, 40)
cloud(100, 200, 60)




"""
cloud.
"""




"""
face = gr.Circle(gr.Point(200, 200), 100)
face.setFill('yellow')

eye1 = gr.Circle(gr.Point(150, 180), 20)
eye2 = gr.Circle(gr.Point(250, 180), 15)
eye1_center = gr.Circle(gr.Point(150, 180), 8)
eye2_center = gr.Circle(gr.Point(250, 180), 7)
eye1.setFill('red')
eye2.setFill('red')
eye1_center.setFill('black')
eye2_center.setFill('black')

eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
eyebrow1.setWidth(10)
eyebrow2.setWidth(10)
eyebrow1.setOutline('black')
eyebrow2.setOutline('black')

mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
mouth.setWidth(20)
mouth.setOutline('black')

face.draw(window)
eye1.draw(window)
eye2.draw(window)
eye1_center.draw(window)
eye2_center.draw(window)
eyebrow1.draw(window)
eyebrow2.draw(window)
mouth.draw(window)
"""
window.getMouse()

window.close()