from tkinter import *

window = Tk()
window.title("Maze")

canvas = Canvas(window, width=700, height=490, bg="black")
canvas.pack()


maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]


for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*70, y*70, (x+1)*70, (y+1)*70, fill="gray", outline="white")


window.mainloop()