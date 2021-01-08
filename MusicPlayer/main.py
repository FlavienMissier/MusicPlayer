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
import time


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
        # self.size = self.audiofile.tag.filesize
        # self.bitRate = self.audiofile.tag.bit-rate
        # self.albumArtist = self.audiofile.tag.b  # error
        # self.dateCreated = self.audiofile.tag.date_created
        # self.dateAddedToLibrary = date_added_to_library
        self.filePath = filepath


class Application:
    isPlaying = False  # True if music is playing
    shuffle = False  # True if shuffle is activated
    repeat = 0  # True if repeat is activated
    pause = False  # True if a song is paused
    mute = False  # True if audio output is muted

    searchEntry = ""  # entry from the search bar
    searchValue = ""

    availableSongs = []  # list of all available songs that can be played
    currentVisiblePlaylist = []  # current list of songs playing in the order seen by the user
    currentPlaylist = []  # current list of songs playing in order that they will be played this is separate from the
    #  visible playlist so that it can be internally shuffled while remaining in the same order for the user
    currentIndexInPlaylist = 0  # index in list of songs currently playing
    selection = []  # selected songs

    player = vlc.MediaPlayer()
    instance = player.get_instance()
    listPlayer = vlc.MediaListPlayer(instance)
    mediaList = vlc.MediaList()

    # play the selected song
    def play_song(self, song):
        self.isPlaying = True
        self.player = vlc.MediaPlayer(song.filePath)
        self.player.play()

    # pause currently playing song to be resumed later
    def pause_or_resume_song(self):
        if self.pause:  # resume song
            self.listPlayer.pause()
            self.pause = False
            self.isPlaying = True
            print("resuming")
        else:  # pause
            self.listPlayer.pause()
            self.pause = True
            self.isPlaying = False
            print("pausing")

    # changes the audio volume, should be an integer 0-100
    def change_volume(self, volume):
        self.player.audio_set_volume(volume)

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

    # inserts a song to current playlist by default adds it to the end
    def insert_song_in_current_playlist(self, song, index=-1):
        if index == -1:
            self.currentPlaylist.append(song)

        if self.listPlayer.is_playing():  # update the list of the current player
            self.mediaList.add_media(song.filePath)
            #self.listPlayer.

    # finds songs and calls add_song_to_library to add them
    def find_songs(self):
        directory = "MusicPlayer\\music files"
        acceptedFileTypes = "mp3 webm"

        for song in os.listdir(directory):
            SongObject = Song(str(os.path.join(directory, song)))
            if (acceptedFileTypes.find(SongObject.fileType)>-1):
                self.currentVisiblePlaylist.append(SongObject)
                self.currentPlaylist.append(SongObject)
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
            # self.play_song(self.currentPlaylist[self.currentIndexInPlaylist])  # old

            self.mediaList = vlc.MediaList(self.currentPlaylist)
            self.listPlayer.set_media_list(self.mediaList)
            self.listPlayer.play()

    # handles what happens after a song has finished playing
    def handle_next_song(self):
        if self.currentIndexInPlaylist >= len(self.currentPlaylist) - 1:  # if the end of the list has been reached
            if self.repeat == 2:
                self.currentIndexInPlaylist = 0
            else:
                self.isPlaying = False
        else:
            self.currentIndexInPlaylist += 1
            
        self.listPlayer.play_item_at_index(self.currentIndexInPlaylist)

    # when the play button is pressed play/pause the current song
    def play_button_pressed(self):
        self.pause_or_resume_song()
        # add visual to show if button is on pause or play

    # goes to the next song
    def next_button_pressed(self):
        self.listPlayer.next()
        # self.handle_next_song()  # old

    # goes to the previous song
    def previous_button_pressed(self):
        self.listPlayer.previous()

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
        # add visual to show if button is pressed or not

    # sets repeat to true/false
    def repeat_button_pressed(self):
        if self.repeat == 1:  # needs to be a 3 state button
            self.repeat = 0
            self.listPlayer.set_playback_mode(0)
        else:
            self.repeat = 0
            self.listPlayer.set_playback_mode(1)
        # add visual to show which state the button is in

    def mute_button_pressed(self):
        if self.mute:
            self.mute = False
            self.player.audio_set_mute(False)
            # self.player.audio_get_mute() may be better to use instead of self.mute
        else:
            self.mute = True
            self.player.audio_set_mute(True)
        # add visual to show if button is pressed or not

    def stop_button_pressed(self):
        self.player.stop()

    def get_data(self):
        print("loading")

    def save_data(self):
        print("saving")

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

        self.muteButton = ttk.Button(root, text='Mute', command=lambda: self.mute_button_pressed())
        self.muteButton.grid(row=4, column=7)

        self.stopButton = ttk.Button(root, text='Stop', command=lambda: self.stop_button_pressed())
        self.stopButton.grid(row=4, column=8)

        self.startButton = ttk.Button(root, text='Start', command=lambda: self.start_playing_list())
        self.startButton.grid(row=4, column=8)
        # need to add volume bar
        # need interactive progress bar

        # test code

        self.selection = ["C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, "
         "Nocturnes, Op 9 No 2.mp3", "C:\\Users\\Flavien "
                                     "Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music "
                                     "files\\Dayglow - Can I Call You Tonight (Official Video).mp3"]
        self.start_playing_list()
        # test code

        # get songs' data from a file if it doesn't exist create it and ask the user for a path to their songs search
        # sub-folders too


root = Tk()

application = Application(root)

root.mainloop()
