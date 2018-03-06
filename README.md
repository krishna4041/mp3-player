->First time when the program executes it walk through each folder in a specied directory and stores all .mp3 files.

This job is done by def get_path_songs(dire) function it return list of songs i.e 'pathofsong#songname'

![get_path_songs](https://user-images.githubusercontent.com/26970266/37051818-8b0b840a-219d-11e8-891d-4a7b49d0fd32.png)

->program execution stars from here.

first it checks whether the song_list file created or not.

when we execute it fist time it raise an exception such that get_path_songs is called and a file is created!

![main_inke_in_mp3](https://user-images.githubusercontent.com/26970266/37052207-a1619978-219e-11e8-9bcd-f6654cf273b8.png)

->created a class named mainframe to handle next song, previous song, pause (buttons) and used some tkinter methods.

![class_mainframe_1](https://user-images.githubusercontent.com/26970266/37052627-e2b07c54-219f-11e8-979d-e0f8df5f997d.png)

![this_not_that](https://user-images.githubusercontent.com/26970266/37052728-1fb4bdd6-21a0-11e8-9d94-dd9f77af1954.png)


when it is executed output will be in this format:
1) three buttons will be present 

![mp3_player_photo](https://user-images.githubusercontent.com/26970266/37053027-1587ba92-21a1-11e8-99aa-07897f506ad4.png)

2)when the pause button is pressed the current song which is playing is paused

3)when pre button is pressed the pointer in lists(which has read all the data from the file created) move up and the song is played

4)when next button is pressed the pointer increments and the song at that position is played

5)the last displayed song denotes the currect song playing.

