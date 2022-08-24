from tkinter import *

def player_move(event):
    if event.keysym == "Up":
        canvas.move(player, 0, -70)

    elif event.keysym == "Down":
        canvas.move(player, 0, 70)

    elif event.keysym == "Left":
        canvas.move(player, -70, 0)

    elif event.keysym == "Right":
        canvas.move(player, 70, 0)

window = Tk()
window.title("Maze")

canvas = Canvas(window, width=700, height=490, bg="light green")
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
            canvas.create_rectangle(x*70, y*70, (x+1)*70, (y+1)*70, fill="cyan", outline="white")

player_image = PhotoImage(file="player.png")
player = canvas.create_image(105,105,image=player_image)

end_image = PhotoImage(file="star.png")
end = canvas.create_image(455,105,image=end_image)

canvas.bind_all("<KeyPress>", player_move)

window.mainloop()