import tkinter as tk
from PIL import ImageTk, Image
import minesweeper

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def on_click(event):
      print("Position = ({0},{1})".format(event.x, event.y))

def on_click(x, y):
      print("Position = " + str(x) + " " + str(y))

root = tk.Tk()
root.title("minesweeper")
width, height = 300, 300
center_window(root, width, height)
tile_dimension = int(width / minesweeper.rows)

# Add widgets (buttons, labels, etc.) and other elements here
mines = minesweeper.get_mines()
for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
             r + c

def draw_images():
    grass_image = Image.open("grass.png")
    grass_image = grass_image.resize((tile_dimension, tile_dimension))
    grass = ImageTk.PhotoImage(grass_image)
    sand_image = Image.open("sand.png")
    sand_image = sand_image.resize((tile_dimension, tile_dimension))
    sand = ImageTk.PhotoImage(sand_image)
    onclick = lambda x, y: (lambda p: on_click(x, y))
    for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
            if mines[r][c] == 0: # or mines[r][c] == 1:
                label1 = tk.Label(image = grass)
                label1.image = grass
                label1.bind('<Button-1>', onclick(r, c))
            elif mines[r][c] == 1: # 2:
                label1 = tk.Label(image = sand)
                label1.image = sand
                label1.bind('<Button-1>', onclick(r, c))
            label1.grid(row = r, column = c)


draw_images()
root.mainloop()
