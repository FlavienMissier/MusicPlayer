# Basic Metadata for music files:
# Title, TrackNumber, Contributing artists, Album, Type, Size, Date created, Date modified, Album artist, Bit rate
# Genre, Length, Protected, Rating, Year

from tkinter import *
from tkinter import ttk


class Application:
    isPlaying = False  # True if music is playing
    shuffle = False  # True if shuffle is activated
    repeat = False  # True if repeat is activated
    pause = False  # True if a song is paused

    searchEntry = ""  # value from the search bar
    searchValue = ""

    availableSongs = []  # list of all available songs that can be played
    currentPlaylist = []  # current list of songs playing
    currentIndexInPlaylist = 0  # index in list of songs currently playing
    selection = []  # selected songs

    currentSongInfo = []  # the current song's name, album, artist, length...


    def play_song(self, song):
        # play the selected song

    def shuffle_songs(self, song_list):
        #shuffle

    def handle_currently_playing(self):
        if self.selection.count() == 0:  # count may not be the right function to find how many things it holds
            print("Select something to play")
        if self.shuffle:
            self.shuffle_songs(self.selection)

        self.play_song(self.selection[0])

    def play_button_pressed(self):
        print("play button pressed")
        self.progressBar.step(10)
        if not self.pause:

        self.play_song(self.selection)
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
        print(self.searchEntry.get())

    def shuffle_button_pressed(self):
        print("shuffle button pressed")

    def repeat_button_pressed(self):
        print("repeat button pressed")
        self.repeat = not self.repeat
        print(self.repeat)

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

        self.repeatButton = ttk.Button(root, text='Repeat', command=lambda: self.repeat_button_pressed())
        self.repeatButton.grid(row=4, column=2)



root = Tk()

application = Application(root)

root.mainloop()
