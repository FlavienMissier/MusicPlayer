#MP3 Player
#By Grayson and Flavien

import eyed3, os, random, pafy

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

playlist = []

while(True):
    if(len(songs) > 0):
        current_song = songs.pop(0)
        audiofile = eyed3.load(current_song)
    else:
        break
    if(sum + audiofile.info.time_secs <= length):
        sum = sum + int(audiofile.info.time_secs)
        playlist.append(current_song)
    elif(len(songs)>0):
        continue
    else:
        break

hours, mins, seconds = convert(sum)

print("\nSongs in your playlist:\n")

for x in playlist:
    audiofile = eyed3.load(x)
    print(audiofile.tag.title)

print("\nHours:", hours)
print("Minutes:", mins)
print("Seconds:", seconds)

myvid = pafy.new("yIcrmHxUuFE")
print("\n" + myvid.title)

myvid2 = myvid.getbestaudio()
myvid2.download(directory, quiet=True)