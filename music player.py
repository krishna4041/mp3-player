import os
from pygame import mixer
from tkinter import *

def get_path_songs(dire):
    store_mp3=[]
    path=os.walk(dire)
    while True:
        try:
            get_files_list=next(path)
            root=get_files_list[0]
            files=get_files_list[2]
            for i in files:
                if ".mp3" in i:
                    store_mp3.append(root+'#'+i)
        except StopIteration:
            break
    return store_mp3

class mainFrame:
    def __init__(self,root):
        self.songs_pos=0
        self.song_pause=0
        self.song_name='MINI MP3 PLAYER'
        frame=Frame(root)
        topframe=Label(root,text=self.song_name)
        topframe.pack()
        frame.pack()
        self.Backbutton=Button(frame,text="<<-",command=self.prevsong)
        self.Backbutton.pack(side=LEFT)
        self.Pausebutton=Button(frame,text="||",command=self.pausesong)
        self.Pausebutton.pack(side=LEFT)
        self.Nextbutton = Button(frame, text="->>", command=self.nextsong)
        self.Nextbutton.pack(side=LEFT)
    def prevsong(self):
        #print("here in prev song")
        if self.songs_pos==0:
            pass
        else:
            self.songs_pos-=1
            cur_song=songs_list[self.songs_pos].strip()
            cur_song=cur_song.split("#")
            self.song_name=cur_song[1]
            topframe = Label(root, text=self.song_name)
            topframe.pack()
            cur_song="\\".join(cur_song)
            mixer.init()
            mixer.music.load(cur_song)
            mixer.music.play()
    def pausesong(self):
        #print("here in pause song")
        if self.song_pause==0:
            mixer.music.pause()
            self.song_pause=1
        elif self.song_pause==1:
            self.song_pause=0
            mixer.music.unpause()

    def nextsong(self):
        print("here in next song")
        if self.songs_pos==len(songs_list):
            pass
        else:
            self.songs_pos+=1
            cur_song=songs_list[self.songs_pos].strip()
            cur_song=cur_song.split("#")
            self.song_name = cur_song[1]
            topframe = Label(root, text=self.song_name)
            topframe.pack()
            cur_song[1]='/'+cur_song[1]
            cur_song="".join(cur_song)
            mixer.init()
            mixer.music.load(cur_song)
            mixer.music.play()



try:
    fl1=open("songslist.txt",'r')
except FileNotFoundError:
    songs_list = get_path_songs(r'D:')
    os.chdir(r'D:')
    fl1 = open("songslist.txt", 'w')
    try:
        for i in songs_list:
            i += '\n'
            fl1.write(i)
    except UnicodeEncodeError:
        pass
    fl1.close()
    fl1 = open("songslist.txt", 'r')

songs_list=fl1.readlines()
#songs_pos=0
root = Tk()
b=mainFrame(root)
root.mainloop()