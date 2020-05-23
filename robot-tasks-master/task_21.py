#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    
    move_right()
    move_down()
    
    a=12
    b=0
    
    while b!=a:
        for i in range(a-b):
            fill_cell()
            move_down()
            fill_cell()
        move_right()    
        for u in range(a-b-1):
            fill_cell()
            move_up()
        b+=1


    fill_cell()
    move_down()
    move_left(n=a)



if __name__ == '__main__':
    run_tasks()
