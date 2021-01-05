#MP3 Player
#By Grayson and Flavien

from mutagen.mp3 import MP3
from mutagen.mp3 import MPEGInfo
import eyed3
import os
import random

# function to convert the seconds into readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

print("\nInput how long you would like the playlist to go to:")
length = int(input())*60

sum = 0
songs = []

directory = "MusicPlayer\\music files"

for song in os.listdir(directory):
    if song.endswith(".mp3"):
        songs.append(str(os.path.join(directory, song)))
    else:
        continue

random.shuffle(songs)

reach_length = True
playlist = []

while(reach_length):
    current_song = songs.pop(0)
    audiofile = eyed3.load(current_song)
    if(sum + audiofile.info.time_secs <= length):
        sum = sum + int(audiofile.info.time_secs)
        playlist.append(current_song)
    elif(len(songs)>0):
        continue
    else:
        reach_length = False

hours, mins, seconds = convert(sum)

print("\nSongs in your playlist:\n")

for x in playlist:
    audiofile = eyed3.load(x)
    print(audiofile.tag.title)

print("\nHours:", hours)
print("Minutes:", mins)
print("Seconds:", seconds)