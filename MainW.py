from tkinter import *
import numpy as np
import time

offset = 10  # 边框宽度
WIN_SIZE_X = 600
WIN_SIZE_Y = 600
CUBE_SIZE = 10
MAX_CELL_X = (int)(WIN_SIZE_X / CUBE_SIZE)
MAX_CELL_Y = (int)(WIN_SIZE_Y / CUBE_SIZE)

CENTER_X = (int)(WIN_SIZE_X / 2)
CENTER_Y = (int)(WIN_SIZE_Y / 2)


def main():
    tk = Tk()
    tk.title('Life Game')
    tk.geometry('1200x700')
    cv = Canvas(tk, width=WIN_SIZE_X + offset * 2, height=WIN_SIZE_Y + offset * 2, bg='black')
    cv.pack()
    world = np.random.randint(0, 2, (MAX_CELL_X, MAX_CELL_Y))

    T_world = world.copy()

    while True:
        cv.delete('rect')
        draw(cv, world, T_world)
        if np.sum(np.abs(world - T_world)) == 0:
            break
        world = T_world.copy()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    rate = (np.sum(world) * 100) / (MAX_CELL_X * MAX_CELL_Y)
    cv.create_text(CENTER_X, CENTER_Y, fill='white', font=20, text="生存率:" + np.str(rate.round(2)) + "%")
    print("生存率:" + np.str(rate.round(2)) + "%")
    tk.mainloop()


def draw(cv, world, T_world):
    for i in range(MAX_CELL_X):
        for j in range(MAX_CELL_Y):
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
