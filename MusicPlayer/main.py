# Basic Metadata for music files:
# Title, TrackNumber, Contributing artists, Album, Type, Size, Date created, Date modified, Album artist, Bit rate
# Genre, Length, Protected, Rating, Year

from tkinter import *
from tkinter import ttk


class Application:
    isPlaying = False
    searchEntry = ""
    searchValue = ""

    def play_button_pressed(self):
        print("play button pressed")
        print(self.searchEntry.get())
        # play the selected songs or playlist

    def next_button_pressed(self):
        print("next button pressed")
        # go back to the

    def previous_button_pressed(self):
        print("previous button pressed")

    def __init__(self, root):
        root.title("Music Player")
        root.geometry("1080x720")
        root.resizable(width=False, height=False)
        # style = ttk.Style
        # style.configure("Style1", foreground="black", background="white")
        # style.configure("TButton", font="Serif 15", padding=10, style="Style1")
        # style.configure("TEntry", font="Serif 18", padding=10, style="Style1")
        self.searchEntry = ttk.Entry(root, textvariable=self.searchValue, width=50)
        self.searchEntry.grid(row=0, columnspan=4, column=2)
        self.button1 = ttk.Button(root, text='7', command=lambda: self.play_button_pressed()).grid(row=1, column=0)


root = Tk()

application = Application(root)

root.mainloop()
