import tkinter as tk
import player
import globals
import pieces

# Create a Tkinter window
root = tk.Tk()
root.title("Vienna Sightreading App")
root.geometry(str(globals.width) + "x" + str(globals.height))
root.configure(bg="#F0F0F0")

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


# Frame für Buttons
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=50)  # Abstand zwischen Buttons

# Text über den Buttons zentriert
welcome_label = tk.Label(button_frame, text="Willkommen bei der Vienna Sightreading App", font=("Arial", 20), bg="#F5F5F5")
welcome_label.pack(pady=20)  # Abstand zwischen Text und Buttons

button_bg_color = "#E0E0E0"  # Hintergrundfarbe der Buttons

violin_button = tk.Button(button_frame,
                          text="Violine",
                          font=("Helvetica", 16),
                          width=20,
                          height=3,
                          command=start_violin,
                          bg="#FFB6C1", fg="#FFFFFF"

                          )
viola_button = tk.Button(button_frame,
                         text="Viola",
                         font=("Helvetica", 16),
                         width=20,
                         height=3,
                         command=start_viola,
                         bg="#FFD700", fg="#FFFFFF"
                         # bg=button_bg_color
                         )
cello_button = tk.Button(button_frame,
                         text="Cello",
                         font=("Helvetica", 16),
                         width=20,
                         height=3,
                         command=start_cello,
                         bg="#00BFFF", fg="#FFFFFF"
                         # bg=button_bg_color
                         )
violin_button.pack(pady=10)
viola_button.pack(pady=10)
cello_button.pack(pady=10)

#logo_image = tk.PhotoImage(file="logo/vsr_logo.png")
#logo_label = tk.Label(root, image=logo_image, bg="#F0F0F0")
#logo_label.pack(pady=20)
# player.start_piece('img/viola/Merry_Go_Round-2.png', root)
root.mainloop()
