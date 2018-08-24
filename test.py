from tkinter import *
import numpy as np
from threading import Thread
import time

offset = 10  # 边框宽度
WIN_SIZE_X = 800
WIN_SIZE_Y = 600
CUBE_SIZE = 10
MAX_CELL_X = (int)(WIN_SIZE_X / CUBE_SIZE)
MAX_CELL_Y = (int)(WIN_SIZE_Y / CUBE_SIZE)

CENTER_X = (int)(MAX_CELL_X / 2)
CENTER_Y = (int)(MAX_CELL_Y / 2)

world = np.random.randint(0, 2, (MAX_CELL_X, MAX_CELL_Y))

T_world = world.copy()


def main():
    itr = 5
    tk = Tk()
    tk.title('Life Game')
    cv = Canvas(tk, width=WIN_SIZE_X + offset * 2, height=WIN_SIZE_Y + offset * 2, bg='black')
    cv.pack()

    while (itr > 0):
        thread_1 = Thread(target=draw, args=(cv, 0, CENTER_Y,))
        thread_2 = Thread(target=draw, args=(cv, CENTER_Y, MAX_CELL_Y,))
        thread_1.setDaemon(True)
        thread_1.start()
        thread_2.setDaemon(True)
        thread_2.start()
        thread_1.join()
        thread_2.join()
        world = T_world.copy()
        itr -= 1
        tk.update_idletasks()
        tk.update()


def draw(cv, bord_up, bord_down):
    cv.delete('rect')
    for i in range(MAX_CELL_X):
        for j in range(bord_up, bord_down):
            if world[i, j] == 1:
                cv.create_rectangle(i * CUBE_SIZE + offset, j * CUBE_SIZE + offset,
                                    (i + 1) * CUBE_SIZE + offset,
                                    (j + 1) * CUBE_SIZE + offset,
                                    fill='white', outline='blue', tags='rect')
            if i == 0 and j == 0:  # 左上角
                aliveCell = world[i + 1, j] + world[i + 1, j + 1] + world[i, j + 1]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X - 1 and j == 0:  # 右上角
                aliveCell = world[i - 1, j] + world[i - 1, j - 1] + world[i, j + 1]
                revelution(T_world, aliveCell, i, j)
            elif i == 0 and j == MAX_CELL_Y - 1:  # 左下角
                aliveCell = world[i, j - 1] + world[i + 1, j - 1] + world[i + 1, j]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X - 1 and j == MAX_CELL_Y - 1:  # 右下角
                aliveCell = world[i - 1, j] + world[i - 1, j - 1] + world[i, j - 1]
                revelution(T_world, aliveCell, i, j)
            elif j == 0:  # 上边界
                aliveCell = world[i - 1, j] + world[i - 1, j + 1] + world[i, j + 1] + world[i + 1, j + 1] + \
                            world[
                                i + 1, j]
                revelution(T_world, aliveCell, i, j)
            elif j == MAX_CELL_Y - 1:  # 下边界
                aliveCell = world[i - 1, j] + world[i - 1, j - 1] + world[i, j - 1] + world[i + 1, j - 1] + \
                            world[
                                i + 1, j]
                revelution(T_world, aliveCell, i, j)
            elif i == 0:  # 左边界
                aliveCell = world[i, j - 1] + world[i + 1, j - 1] + world[i + 1, j] + world[i + 1, j + 1] + \
                            world[
                                i, j + 1]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X - 1:  # 右边界
                aliveCell = world[i, j - 1] + world[i - 1, j - 1] + world[i - 1, j] + world[i - 1, j + 1] + \
                            world[
                                i, j + 1]
                revelution(T_world, aliveCell, i, j)
            else:
                aliveCell = world[i - 1, j - 1] + world[i, j - 1] + world[i + 1, j - 1] + world[i - 1, j] + \
                            world[
                                i + 1, j] + world[i - 1, j + 1] + world[i, j + 1] + world[i + 1, j + 1]
                revelution(T_world, aliveCell, i, j)


def revelution(T_world, aliveCell, i, j):
    if aliveCell == 3:
        T_world[i, j] = 1
    elif aliveCell != 2:
        T_world[i, j] = 0


main()
