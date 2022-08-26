from tkinter import *
from tkinter import messagebox
import random

def player_move(event):
    global x, y, num

    if event.keysym == "Up" and maze[num][y-1][x] != 1:
        canvas.move(player, 0, -70)
        y -= 1
    
    elif event.keysym == "Down" and maze[num][y+1][x] != 1:
        canvas.move(player, 0, 70)
        y += 1

    elif event.keysym == "Left" and maze[num][y][x-1] != 1:
        canvas.move(player, -70, 0)
        x -= 1

    elif event.keysym == "Right" and maze[num][y][x+1] != 1:
        canvas.move(player, 70, 0)
        x += 1

    if maze[num][y][x] == 2:
        messagebox.showinfo("Complete", "You have reached the destination.")

window = Tk()
window.title("Maze")

canvas = Canvas(window, width=700, height=490, bg="light green")
canvas.pack()

maze = [
    [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,1,1,2,0,0,1],  # 2 is the destination
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,0,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ],

    [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,2,1,1,1],
    [1,0,1,0,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ],

    [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,2,1,1,1],
    [1,1,1,0,1,0,0,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ],

    [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,2,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,1,0,1,0,0,0,1,0,1],
    [1,1,0,1,0,1,0,1,0,1],
    [1,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]
]

num = random.randint(0, len(maze)-1)

for y in range(7):
    for x in range(10):
        if maze[num][y][x] == 1:
            canvas.create_rectangle(x*70, y*70, (x+1)*70, (y+1)*70, fill="cyan", outline="white")

x = 1
y = 1

player_image = PhotoImage(file="player.png")
player = canvas.create_image(105,105,image=player_image)

end_image = PhotoImage(file="star.png")
end = canvas.create_image(455,105,image=end_image)

canvas.bind_all("<KeyPress>", player_move)

window.mainloop()