#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

    
    move_down()
    move_right()
    while wall_is_on_the_right() is False:
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_left()
        move_left()
        fill_cell()
        
        a=0
        while wall_is_on_the_right() is False and a<5:
            move_right()
            a+=1
        move_up()
    move_left(n=2)

if __name__ == '__main__':
    run_tasks()
