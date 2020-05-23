#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    while wall_is_on_the_right() is False:
        if wall_is_above() is True and wall_is_beneath() is True:
            fill_cell()
            move_right()
        else:
            move_right()
    if wall_is_on_the_right() is True and (wall_is_above() is True and wall_is_beneath() is True):
        fill_cell()


if __name__ == '__main__':
    run_tasks()
