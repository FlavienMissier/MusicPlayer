# Basic Metadata for music files:
# Title, TrackNumber, Contributing artists, Album, Type, Size, Date created, Date modified, Album artist, Bit rate
# Genre, Length, Protected, Rating, Year

from tkinter import *
from tkinter import ttk


class Application:
    isPlaying = False
    searchEntry = ""
    searchValue = ""
    selection = []

    def play_button_pressed(self):
        print("play button pressed")
        print(self.searchEntry.get())
        self.progressBar.step(10)
        # play the selected songs or playlist

    def next_button_pressed(self):
        print("next button pressed")
        # go to the next song

    def previous_button_pressed(self):
        print("previous button pressed")
        # go to the previous song or go back to beginning of song if it has been playing for long enough
        self.progressBar.step(-10)

    def search_button_pressed(self):
        print("search button pressed")

    def __init__(self, root):
        root.title("Music Player")
        root.geometry("1080x720")
        root.resizable(width=False, height=False)
        style = ttk.Style
        # style.configure("Style1", foreground="black", background="white")
        # style.configure("TButton", font="Serif 15", padding=10, style="Style1")
        # style.configure("TEntry", font="Serif 18", padding=10, style="Style1")

        self.searchEntry = ttk.Entry(root, textvariable=self.searchValue, width=50)
        self.searchEntry.grid(row=0, columnspan=4, column=2)

        self.searchButton = ttk.Button(root, text='Search', command=lambda: self.search_button_pressed())
        self.searchButton.grid(row=0, column=5)

        self.playButton = ttk.Button(root, text='Play', command=lambda: self.play_button_pressed())
        self.playButton.grid(row=4, column=4)

        self.nextButton = ttk.Button(root, text='Next', command=lambda: self.next_button_pressed())
        self.nextButton.grid(row=4, column=5)

        self.previousButton = ttk.Button(root, text='Previous', command=lambda: self.previous_button_pressed())
        self.previousButton.grid(row=4, column=3)

        self.progressBar = ttk.Progressbar(root, length=1000)
        self.progressBar.grid(row=10, columnspan=10, column=0)

root = Tk()

application = Application(root)

root.mainloop()
