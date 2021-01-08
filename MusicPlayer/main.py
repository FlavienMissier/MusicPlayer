# MP3 Player
# By Grayson and Flavien

from tkinter import *
from tkinter import ttk
import eyed3
import pafy
import os
os.add_dll_directory("C:\\Program Files\\VideoLAN\\VLC")
import random
import vlc


class Song:
    audiofile = ""
    title = ""
    artist = ""
    album = ""
    trackNumber = ""
    length = ""
    genre = ""
    year = ""
    rating = ""
    albumArtist = ""
    # bitRate = ""
    # size = ""
    # dateCreated = ""  # date the file was created
    # dateAddedToLibrary = ""  # date the song was added to the music player's library
    fileType = ""
    filePath = ""  # path to the song file

    def __init__(self, filepath=""):
        splitfile = filepath.split(".")
        self.audiofile = eyed3.load(filepath)
        self.fileType = splitfile[len(splitfile)-1]
        self.year = self.audiofile.tag.original_release_date
        self.genre = self.audiofile.tag.genre
        self.length = self.audiofile.info.time_secs
        #self.trackNumber = self.audiofile.tag.track
        self.album = self.audiofile.tag.album
        self.artist = self.audiofile.tag.artist
        self.title = self.audiofile.tag.title
        self.rating = self.audiofile.tag.popularities
        #self.size = self.audiofile.tag.filesize
        #self.bitRate = self.audiofile.tag.bit-rate
        #self.albumArtist = self.audiofile.tag.b
        #self.dateCreated = self.audiofile.tag.date_created
        #self.dateAddedToLibrary = date_added_to_library
        self.filePath = filepath


class Application:
    isPlaying = False  # True if music is playing
    shuffle = False  # True if shuffle is activated
    repeat = False  # True if repeat is activated
    pause = False  # True if a song is paused

    searchEntry = ""  # entry from the search bar
    searchValue = ""

    availableSongs = []  # list of all available songs that can be played
    currentVisiblePlaylist = []  # current list of songs playing in the order seen by the user
    currentPlaylist = []  # current list of songs playing in order that they will be played this is separate from the
    #  visible playlist so that it can be internally shuffled while remaining in the same order for the user
    currentIndexInPlaylist = 0  # index in list of songs currently playing
    selection = []  # selected songs

    player = vlc.MediaPlayer()

    # play the selected song
    def play_song(self, song):
        self.isPlaying = True
        self.player = vlc.MediaPlayer(song.filePath)
        self.player.play()

        print("play song")

    # pause currently playing song to be resumed later
    def pause_or_resume_song(self):
        if self.pause:  # resume song
            self.player.pause()
            self.pause = False
            self.isPlaying = True
            print("resuming")
        else:  # pause
            self.player.pause()
            self.pause = True
            self.isPlaying = False
            print("pausing")

    # changes the audio volume
    def change_volume(self, volume):
        print("change volume")

    # gets song data from the file given the path to that file and returns a Song object using that data
    def get_song_data(self, path):
        song = Song(filepath=path)  # check if path is correct then get data
        return song

    # adds song to the library given the path calling get_song_data to get the data
    def add_song_to_library(self, song_path):
        new_song = self.get_song_data(song_path)  # check if path is correct
        self.availableSongs.append(new_song)
        # also add songs and their data to a file

    def add_song_to_list(self, song, song_list):
        if song.length != 0:  # perform checks to make sure song is playable check for proper song type and if it exists
            song_list.append(song)

    # finds songs and calls add_song_to_library to add them
    def find_songs(self):
        directory = "MusicPlayer\\music files"
        acceptedFileTypes = "mp3 webm"

        print("wut")

        for song in os.listdir(directory):
            SongObject = Song(str(os.path.join(directory, song)))
            if (acceptedFileTypes.find(SongObject.fileType)>-1):
                self.currentVisiblePlaylist.append(SongObject)
                self.currentPlaylist.append(SongObject)
                print(SongObject.title)
            else:
                continue

    # sorts songs, attribute is the attribute to be sorted by, song_list is the list to sort, and reverse decides
    # whether the songs will be sorted in ascending or descending order
    def sort_songs_by(self, attribute, song_list, reverse):
        print("sorting songs by attribute: ", attribute)

    # puts the selected songs in a list to be played and starts playing it
    def start_playing_list(self):
        if len(self.selection) == 0:  # if the list is empty
            print("Select something to play")
        else:
            if self.shuffle:
                random.shuffle(self.selection)

            self.currentPlaylist = self.selection
            self.currentVisiblePlaylist = self.currentPlaylist
            self.currentIndexInPlaylist = 0
            self.play_song(self.currentPlaylist[self.currentIndexInPlaylist])

    # handles what happens after a song has finished playing
    def handle_next_song(self):
        if self.currentIndexInPlaylist >= len(self.currentPlaylist) - 1:  # if the end of the list has been reached
            if self.repeat:
                self.currentIndexInPlaylist = 0
            else:
                self.isPlaying = False
        else:
            print("yo")
            self.currentIndexInPlaylist += 1

        print(self.currentIndexInPlaylist)
        print(self.currentPlaylist[self.currentIndexInPlaylist].title)
        self.play_song(self.currentPlaylist[self.currentIndexInPlaylist])

    # when the play button is pressed play/pause the current song
    def play_button_pressed(self):
        self.pause_or_resume_song()
        self.playButton.keys()
        # add visual to show if button is on pause or play

    # goes to the next song
    def next_button_pressed(self):
        self.player.stop()
        self.handle_next_song()

    # goes to the previous song or goes back to beginning of song if it has been playing for long enough
    def previous_button_pressed(self):
        print("previous button pressed")
        self.player.play()

    # searches for matching song/authors/albums using the entry
    def search_button_pressed(self):
        songSearched = pafy.new(self.searchEntry.get())
        newSong = songSearched.getbestaudio()
        newSong.download("C:\\Users\\vidrinen\\Documents\\GitHub\\MusicPlayer\\MusicPlayer\\music files", quiet=True)

    # sets shuffle to true/false
    def shuffle_button_pressed(self):
        print("shuffle button pressed")
        if self.shuffle:
            self.shuffle = False
            self.currentPlaylist = self.currentVisiblePlaylist
        else:
            self.shuffle = True
            random.shuffle(self.currentPlaylist)  # perhaps exclude already played songs?
        print(self.shuffle)
        # add visual to show if button is pressed or not

    # sets repeat to true/false
    def repeat_button_pressed(self):
        print("repeat button pressed")
        self.repeat = not self.repeat
        print(self.repeat)
        # add visual to show if button is pressed or not

    def __init__(self, root):
        self.find_songs()

        # creating the window
        root.title("Music Player")
        root.geometry("1080x720")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("Style1", foreground="black", background="white")
        style.configure("TButton", font="Serif 10", padding=4)
        style.configure("TEntry", font="Serif 12", padding=4)

        # adding all the buttons and widgets
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

        self.shuffleButton = ttk.Button(root, text='Shuffle', command=lambda: self.shuffle_button_pressed())
        self.shuffleButton.grid(row=4, column=6)

        # test stuff

        song1 = Song("C:\\Users\\vidrinen\\Documents\\GitHub\\MusicPlayer\\MusicPlayer\\music files\\Chopin, Nocturnes, Op 9 No 2.mp3")
        song2 = Song("C:\\Users\\vidrinen\\Documents\\GitHub\\MusicPlayer\\MusicPlayer\\music files\\Dayglow - Can I Call You Tonight (Official Video).mp3")

        self.selection.append(song1)
        self.selection.append(song2)
        self.player.play()

        self.start_playing_list()

        #media1 = vlc.Media("C:\\Users\\vidrinen\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, Nocturnes, Op 9 No 2.mp3")
        #medialist = vlc.MediaList(self.selection)

        #media1.
        # test stuff

        # get songs' data from a file if it doesn't exist create it and ask the user for a path to their songs search
        # sub-folders too


root = Tk()

application = Application(root)

root.mainloop()
