import tkinter as tk
import player
import globals
import pieces


# Create a Tkinter window
root = tk.Tk()
root.title("test")
root.geometry(str(globals.width) + "x" + str(globals.height))

button_frame = tk.Frame(root)
button_frame.pack()


def start_violin():
    button_frame.pack_forget()
    pieces.show_pieces('violin', root)

def start_viola():
    button_frame.pack_forget()
    pieces.show_pieces('viola', root)

def start_cello():
    button_frame.pack_forget()
    pieces.show_pieces('cello', root)

violin_button = tk.Button(button_frame,
                         text="violin",
                         command=start_violin)
viola_button = tk.Button(button_frame,
                         text="viola",
                         command=start_viola)
cello_button = tk.Button(button_frame,
                         text="cello",
                         command=start_cello)
violin_button.pack()
viola_button.pack()
cello_button.pack()

# player.start_piece('img/viola/Merry_Go_Round-2.png', root)
root.mainloop()