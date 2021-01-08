# MP3 Player
# By Grayson and Flavien

import eyed3
import os
import random
import pafy
import vlc
import time
from tkinter import ttk

'''# function to convert the seconds into readable format
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
    elif len(songs)>0:
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
'''



list1 = ["C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, "
         "Nocturnes, Op 9 No 2.mp3", "C:\\Users\\Flavien "
                                     "Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music "
                                     "files\\Dayglow - Can I Call You Tonight (Official Video).mp3"]

media1 = vlc.Media(
    "C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, Nocturnes, Op 9 No 2.mp3")
medialist = vlc.MediaList(list1)
medialistplayer = vlc.MediaListPlayer()
medialistplayer.set_media_list(medialist)
mediaplayer = vlc.MediaPlayer("C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, Nocturnes, Op 9 No 2.mp3")
mediaplayer.play()
medialistplayer = vlc.MediaListPlayer(mediaplayer.get_instance())
medialistplayer.set_media_list(medialist)
medialistplayer.play()

time.sleep(1000)


media1.parse()
print(media1.get_duration() / 1000)  # duration in ms of song

# media1.tracks_get()
# vlc.libvlc_media_tracks_release() # can't get that to work for now

print(medialist.count())
medialist.item_at_index(0)  # returns media object at that index
medialist.add_media(
    "C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Dayglow - Hot Rod (Official Video).mp3")
#  medialist.insert_media()

mediaplayer = vlc.MediaPlayer(
    "C:\\Users\\Flavien Missier\\Desktop\\code\\python\\MusicPlayer\\MusicPlayer\\music files\\Chopin, Nocturnes, Op 9 No 2.mp3")
mediaplayer.play()
print("length: ", mediaplayer.get_length())
mediaplayer.set_time(30)
print("time: ", mediaplayer.get_time())
mediaplayer.set_position(0.3)
print("position: ", mediaplayer.get_position())
mediaplayer.will_play()  # is the player able to play, idk exactly what that means
print(mediaplayer.get_rate())
mediaplayer.set_rate(1)  # set speed 1 seems to be normal
mediaplayer.get_state()  # {0: 'NothingSpecial',1: 'Opening',2: 'Buffering',3: 'Playing',4: 'Paused',5: 'Stopped',6: 'Ended', 7: 'Error'}
print(mediaplayer.audio_output_device_enum())  #
# mediaplayer.audio_output_device_set()
print(mediaplayer.audio_output_device_get())
print(mediaplayer.audio_get_mute())
mediaplayer.audio_set_mute(False)
print(mediaplayer.audio_get_volume())  # 0-100
mediaplayer.audio_set_volume(50)  # 0-100

mediaplayerlist = vlc.MediaListPlayer()
mediaplayerlist.set_media_player(mediaplayer)
mediaplayerlist.get_media_player()
mediaplayerlist.set_media_list(medialist)
mediaplayerlist.play()
mediaplayerlist.pause()
mediaplayerlist.is_playing()
mediaplayerlist.get_state()
mediaplayerlist.play_item_at_index(1)
mediaplayerlist.previous()
mediaplayerlist.next()
mediaplayerlist.set_playback_mode(0)  # 0: 'default', 1: 'loop', 2: 'repeat'}  # repeat is for repeating the
# current song even if there are other songs in the playlist
mediaplayerlist.stop()

instance = mediaplayerlist.get_instance()

instance.vlm_del_media()
instance.audio_output_enumerate_devices()
instance.audio_output_list_get()
instance.media_library_new()
instance.media_discoverer_new()

instance.media_new_location()
instance.media_new_path()
instance.media_new()  # can be URL or path

instance.media_discoverer_list_get()
instance.vlm_set_loop()
