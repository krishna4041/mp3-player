import os
import pygame
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

class mainFrame(Frame):

    def __init__(self,master):
        super(mainFrame, self).__init__(master)
        self.songs_pos=0
        self.song_pause=0
        self.point=1
        self.playlistbox = Listbox(self, width=60, height=10,selectmode=SINGLE)
        for song in songs_list:
            song=song.split("#")
            song=song[1]
            self.playlistbox.insert(END, song)
        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row=1)
       # self.top1frame=Label(root,bg="white",text=self.song_name)
        self.PlayallButton = Button(self, text='play', command=self.play)
        self.prevButton = Button(self, text='prev', command=self.prevsong)
        self.pauseButton = Button(self, text='pause', command=self.pausesong)
        self.nextButton = Button(self, text='next', command=self.nextsong)
        self.PlayallButton.grid(row=4, column=0)
        self.prevButton.grid(row=4, column=1)
        self.pauseButton.grid(row=4, column=2)
        self.nextButton.grid(row=4, column=3)
        self.pack()

    def play(self):
        pygame.init()
        selected_song= self.playlistbox.curselection()
        self.songs_pos=selected_song[0]
        cur_song = songs_list[selected_song[0]].strip()
        cur_song = cur_song.split("#")
        self.song_name = cur_song[1]
        cur_song[1] = '\\' + cur_song[1]
        cur_song = "".join(cur_song)
        pygame.mixer.init()
        pygame.mixer.music.load(cur_song)
        pygame.mixer.music.play()
        if self.point == 1:
            self.topframe = Label(root, text=self.song_name)
        else:
            self.topframe.config(text=self.song_name)
        self.topframe.pack()
        self.point+=1

    def prevsong(self):
        #print("here in prev song")
        if self.songs_pos==0:
            pass
        else:
            self.songs_pos-=1
            cur_song=songs_list[self.songs_pos].strip()
            cur_song=cur_song.split("#")
            self.song_name=cur_song[1]
            if self.point==1:
                self.topframe = Label(root,text=self.song_name)
            else:
                self.topframe.config(text=self.song_name)
            self.topframe.pack()
            cur_song="\\".join(cur_song)
            pygame.mixer.init()
            pygame.mixer.music.load(cur_song)
            pygame.mixer.music.play()
            self.point+=1

    def pausesong(self):
        #print("here in pause song")
        if self.song_pause==0:
            pygame.mixer.music.pause()
            self.song_pause=1
        elif self.song_pause==1:
            self.song_pause=0
            pygame.mixer.music.unpause()

    def nextsong(self):
        print("here in next song")
        if self.songs_pos==len(songs_list):
            pass
        else:
            self.songs_pos+=1
            cur_song=songs_list[self.songs_pos].strip()
            cur_song=cur_song.split("#")
            self.song_name = cur_song[1]
            if self.point==1:
               self.topframe = Label(root,text=self.song_name)
            else:
                self.topframe.config(text=self.song_name)
            self.topframe.pack()
            cur_song[1]='/'+cur_song[1]
            cur_song="".join(cur_song)
            pygame.mixer.init()
            pygame.mixer.music.load(cur_song)
            pygame.mixer.music.play()
            self.point+=1

if __name__ == '__main__':
    try:
        fl1=open("songslist.txt",'r')
    except FileNotFoundError:
        songs_list = get_path_songs(r'D:')
        os.chdir(r'D:')
        fl1 = open("songslist.txt", 'w')
        try:
            for song in songs_list:
                song += '\n'
                fl1.write(song)
        except UnicodeEncodeError:
            pass
        fl1.close()
        fl1 = open("songslist.txt", 'r')

    songs_list=fl1.readlines()
    root = Tk()
    root.title('MP3 PLAYER')
    root.geometry('500x250')
    b=mainFrame(root)
    b.mainloop()