import tkinter as tk
from PIL import ImageTk, Image
import minesweeper

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def on_left_grass_click(x, y):
      minesweeper.dig(x, y)
      for label in labels: label.destroy()
      draw_images()

def on_right_grass_click(x, y):
    minesweeper.flag(x, y)
    for label in labels: label.destroy()
    draw_images()

def on_flag_click(x, y):
    minesweeper.unflag(x, y)
    for label in labels: label.destroy()
    draw_images()

# different colours for each number


root = tk.Tk()
root.title("minesweeper")
width, height = 300, 300
center_window(root, width + (minesweeper.rows * 4 + 1), height + (minesweeper.columns * 4 + 1))
tile_dimension = int(width / minesweeper.rows)

# Add widgets (buttons, labels, etc.) and other elements here
mines = minesweeper.get_mines()
for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
             r + c

sand_x_images = []

# -1 covered no mine, -2 covered mine, -3 uncovered mine, otherwise num of mines around
def draw_images():  
    grass_image = Image.open("res/grass.png")
    grass_image = grass_image.resize((tile_dimension, tile_dimension))
    grass = ImageTk.PhotoImage(grass_image)
    sand_image = Image.open("res/sand.png")
    sand_image = sand_image.resize((tile_dimension, tile_dimension))
    sand = ImageTk.PhotoImage(sand_image)
    bomb_image = Image.open("res/bomb.png")
    bomb_image = bomb_image.resize((tile_dimension, tile_dimension))
    bomb = ImageTk.PhotoImage(bomb_image)
    flag_image = Image.open("res/flag.png")
    flag_image = flag_image.resize((tile_dimension, tile_dimension))
    flag = ImageTk.PhotoImage(flag_image)
    for x in range(0, 9):
         file_name = ("res/sand-" + str(x) + ".png")
         sand_image_x = Image.open(file_name)
         sand_image_x = sand_image_x.resize((tile_dimension, tile_dimension))
         sand_x_images.append(ImageTk.PhotoImage(sand_image_x))  
    left_grass_click = lambda x, y: (lambda p: on_left_grass_click(x, y))
    right_grass_click = lambda x, y: (lambda p: on_right_grass_click(x, y))
    flag_click = lambda x, y: (lambda p: on_flag_click(x, y))
    for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
            if minesweeper.is_covered(r, c): # covered
                label1 = tk.Label(image = grass)
                label1.image = grass
                label1.bind('<Button-1>', left_grass_click(r, c))
                label1.bind('<Button-2>', right_grass_click(r, c))
                labels.append(label1)
            elif minesweeper.is_flag(r, c): # flag
                label1 = tk.Label(image = flag)
                label1.image = flag
                label1.bind('<Button->', flag_click(r, c))
                labels.append(label1)
            elif mines[r][c] == -2: # uncovered bomb
                label1 = tk.Label(image = bomb)
                label1.image = bomb
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
