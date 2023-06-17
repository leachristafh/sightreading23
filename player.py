import tkinter as tk
import globals


def start_piece(path, frame):
    # Create a Label widget to display the image
    canvas = tk.Canvas(frame, width=globals.width, height=globals.height-50, bg="white")
    canvas.pack()

    slider = tk.Scale(frame, from_=0, to=50, orient=tk.HORIZONTAL)
    slider.pack()

    image = tk.PhotoImage(file=path)
    piece = canvas.create_image(500, 200, anchor=tk.NW, image=image)

    #canvas.create_line(200, 0, 200, globals.height, fill="red", width=2)


    def move_left():
        canvas.move(piece, -slider.get()/5, 0)
        canvas.after(20, move_left)


    move_left()

    # Start the Tkinter event loop
    frame.mainloop()