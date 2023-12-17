import tkinter as tk
from PIL import ImageTk, Image
import minesweeper

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def on_click(x, y):
      minesweeper.dig(x, y)
      for label in labels: label.destroy()
      draw_images()

# make a list of sand number images to you don't need so many elifs
# different colours for each number


root = tk.Tk()
root.title("minesweeper")
width, height = 300, 300
center_window(root, width + 21, height + 21)
tile_dimension = int(width / minesweeper.rows)

# Add widgets (buttons, labels, etc.) and other elements here
mines = minesweeper.get_mines()
for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
             r + c

sand_x_images = []

# -1 covered no mine, -2 covered mine, -3 uncovered mine, otherwise num of mines around
def draw_images():  
    grass_image = Image.open("grass.png")
    grass_image = grass_image.resize((tile_dimension, tile_dimension))
    grass = ImageTk.PhotoImage(grass_image)
    sand_image = Image.open("sand.png")
    sand_image = sand_image.resize((tile_dimension, tile_dimension))
    sand = ImageTk.PhotoImage(sand_image)
    bomb_image = Image.open("bomb.png")
    bomb_image = bomb_image.resize((tile_dimension, tile_dimension))
    bomb = ImageTk.PhotoImage(bomb_image)
    for x in range(0, 9):
         file_name = ("sand-" + str(x) + ".png")
         sand_image_x = Image.open(file_name)
         sand_image_x = sand_image_x.resize((tile_dimension, tile_dimension))
         sand_x_images.append(ImageTk.PhotoImage(sand_image_x))  
    onclick = lambda x, y: (lambda p: on_click(x, y))
    for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
            if minesweeper.is_covered(r, c): # covered
                label1 = tk.Label(image = grass)
                label1.image = grass
                label1.bind('<Button-1>', onclick(r, c))
                labels.append(label1)
            elif mines[r][c] == -2: # uncovered bomb
                label1 = tk.Label(image = bomb)
                label1.image = bomb
                label1.bind('<Button-1>', onclick(r, c))
                labels.append(label1)
            else: # uncovered sand
                index = mines[r][c]
                label1 = tk.Label(image = sand_x_images[index])
                label1.image = sand_x_images[index]
                labels.append(label1)    
            label1.grid(row = r, column = c)

labels = []
draw_images()
root.mainloop()
