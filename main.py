import tkinter as tk
from PIL import ImageTk, Image
from pynput import mouse
import minesweeper

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

window = tk.Tk()
window.title("minesweeper")
width, height = 300, 300
center_window(window, width, height)

grass = ImageTk.PhotoImage(Image.open("grass.png"))
label = tk.Label(image=grass)
label.image = grass
# Position image
label.place(x=0, y=0)

# Add widgets (buttons, labels, etc.) and other elements here
mines = minesweeper.get_mines()
for r in range(minesweeper.rows):
        for c in range(minesweeper.columns):
             r + c
            # button = tk.Button(window, command = minesweeper.hit(r, c))
            # button.place(x=r*(width/minesweeper.rows), y=c*(width/minesweeper.columns))

def on_click(x, y, button, pressed):
    if 'Pressed':
         minesweeper.click(round(x), round(y))
    return False
    

listener = mouse.Listener(on_click=on_click)
listener.start()

window.mainloop()
