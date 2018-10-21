#requires pyglet and avbin.
"""
Plays all the .mp3 files in the same directory, in random order, endlessly.
"""
import pyglet, os, time, random
music_files = []#list to hold all the music files in the directory.
for file_name in os.listdir('.'):
    if file_name[-4:] == ".mp3":
        music_files.append(str(file_name))#append all mp3 files to music_files
player = pyglet.media.Player()
first_song = True#keeps track of if the player was just created or not.
while True:
    time.sleep(1)
    if player.time == 0.0:
        choice = random.choice(music_files)#picks a random song name.
        print ("Playing Song: "+str(choice))
        source = pyglet.media.load(choice)
        player.queue(source)#add the source to the queue
        if not first_song:#player.next() is called to play the next song
            player.next()#  after the song before has finished playing.
        else:
            player.play()#starts the first song playing.
            first_song = False
