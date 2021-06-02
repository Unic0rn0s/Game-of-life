import numpy as np
import tkinter


HEIGHT = 500
WIDTH = 500
SIZE = 10


def draw(event):
    global population
    canvas.delete('all')
    for i in range(len(population)):
        for j in range(len(population[i])):
            if population[i][j]:
                canvas.create_rectangle((i * SIZE, j * SIZE), (i * SIZE + SIZE, j * SIZE + SIZE), fill='green')
    population = next_population(population)


def add_square(event):
    x, y = event.x, event.y
    x_pp, y_pp = x // SIZE, y // SIZE
    if x_pp < 50 and y_pp < 50:
        population[x_pp][y_pp] = 1
        canvas.create_rectangle((x_pp * SIZE, y_pp * SIZE), (x_pp * SIZE + SIZE, y_pp * SIZE + SIZE), fill='green')


def next_population(population):
    neighbors = sum([
     np.roll(np.roll(population, -1, 1), 1, 0),
     np.roll(np.roll(population, 1, 1), -1, 0),
     np.roll(np.roll(population, 1, 1), 1, 0),
     np.roll(np.roll(population, -1, 1), -1, 0),
     np.roll(population, 1, 1),
     np.roll(population, -1, 1),
     np.roll(population, 1, 0),
     np.roll(population, -1, 0)
    ])
    return (neighbors == 3) | (population & (neighbors == 2))


population = np.array(
     [[0] * 50 for _ in range(50)], dtype=np.uint8)


master = tkinter.Tk()
master.title('Game of life v0.1')
canvas = tkinter.Canvas(master, bg='white', height=HEIGHT, width=WIDTH)
canvas.pack()
master.bind('<KeyPress>', draw)
canvas.bind('<Button-1>', add_square)
canvas.bind('<B1-Motion>', add_square)
label = tkinter.Label(master, text='To start, hold down any key. You can draw while moving.')
label.pack()
master.mainloop()
