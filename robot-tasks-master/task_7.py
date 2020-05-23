#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() is False:
        move_down()
    if wall_is_beneath() is True:
        while wall_is_beneath():
            move_right()
            if wall_is_beneath() is False:
                move_down()
                move_left()
                if wall_is_above() is True:
                    while wall_is_above() is True and wall_is_on_the_left() is False:
                        move_left()
   

if __name__ == '__main__':
    run_tasks()
