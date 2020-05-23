import graphics as gr

window = gr.GraphWin("Scene 1", 1000, 1000)

sun=gr.Circle(gr.Point(800, 200), 75)
sun.setFill('yellow')
sun.setOutline('yellow')
sun.draw(window)

radians1=gr.Line(gr.Point(800, 300), gr.Point(800, 390))
radians1.setOutline('yellow')
radians1.setWidth(15)
radians1.draw(window)

radians2=gr.Line(gr.Point(730, 273), gr.Point(669, 337))
radians2.setOutline('yellow')
radians2.setWidth(15)
radians2.draw(window)

radians3=gr.Line(gr.Point(700, 211), gr.Point(600, 240))
radians3.setOutline('yellow')
radians3.setWidth(15)
radians3.draw(window)

radians4=gr.Line(gr.Point(706, 148), gr.Point(600, 96))
radians4.setOutline('yellow')
radians4.setWidth(15)
radians4.draw(window)








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

window.getMouse()

window.close()