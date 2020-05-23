#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    a=0
    
    while a<3 and wall_is_on_the_right() is False:
        move_right()
        if cell_is_filled() is True:
            a+=1
        else:
            a=0

if __name__ == '__main__':
    run_tasks()
