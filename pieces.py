import tkinter as tk
import player

class Piece():
    def __init__(self, name, path):
        self.name = name
        self.path = path

def instrument_pieces(instrument):
    if instrument == 'violin':
        return [
            Piece(
                'Paganini Caprice',
                'img/violin/paganini_caprice-2.png'
            ),
            Piece(
                'Stück 2',
                'img/violin/paganini_caprice-2.png'
            ),
            Piece(
                'Stück 3',
                'img/violin/paganini_caprice-2.png'
            )
        ]
    elif instrument == 'viola':
        return [
            Piece(
                'Merry go round',
                'img/viola/Merry_Go_Round-2.png'
            ),
            Piece(
                'Stück 2',
                'img/violin/paganini_caprice-2.png'
            )
        ]
    elif instrument == 'cello':
        return [
            Piece(
                'Schosta',
                'img/cello/celloschosta-2.png'
            ),
            Piece(
                'Stück 2',
                'img/viola/Merry_Go_Round-2.png'
            )
        ]
def show_pieces(instrument, frame):
    button_frame = tk.Frame(frame)
    button_frame.pack()

    for piece in instrument_pieces(instrument):
        name = piece.name
        path = piece.path

        def start_piece(current_path = path):
            button_frame.pack_forget()
            player.start_piece(current_path, frame)

        piece_button = tk.Button(button_frame,
                                  text=name,
                                  command=start_piece)

        piece_button.pack()

    frame.mainloop()