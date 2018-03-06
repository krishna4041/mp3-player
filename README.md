->First time when the program executes it walk through each folder in a specied directory and stores all .mp3 files.

This job is done by def get_path_songs(dire) function it return list of songs i.e 'pathofsong#songname'

![get_path_songs](https://user-images.githubusercontent.com/26970266/37051818-8b0b840a-219d-11e8-891d-4a7b49d0fd32.png)

->program execution stars from here.

first it checks whether the song_list file created or not.

when we execute it fist time it raise an exception such that get_path_songs is called and a file is created!

![main_inke_in_mp3](https://user-images.githubusercontent.com/26970266/37052207-a1619978-219e-11e8-9bcd-f6654cf273b8.png)

->created a class named mainframe to handle next song, previous song, pause (buttons) and used some tkinter methods.

![class_mainframe_1](https://user-images.githubusercontent.com/26970266/37052627-e2b07c54-219f-11e8-979d-e0f8df5f997d.png)
