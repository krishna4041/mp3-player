->First time when the program executes it walk through each folder in a specied directory and stores all .mp3 files.

This job is done by def get_path_songs(dire) function it return list of songs i.e 'pathofsong#songname'

![get_path_songs](https://user-images.githubusercontent.com/26970266/37051818-8b0b840a-219d-11e8-891d-4a7b49d0fd32.png)

->program execution stars from here.

first it checks whether the song_list file created or not.

when we execute it fist time it raise an exception such that get_path_songs is called and a file is created!

![mian_func_mp3_player](https://user-images.githubusercontent.com/26970266/37195210-d802a2ce-2397-11e8-80ba-01d12cb776fa.png)


->created a class named mainframe to handle play,next song, previous song, pause (buttons) and used some tkinter methods.

![min_class_](https://user-images.githubusercontent.com/26970266/37195311-4c245490-2398-11e8-9bb5-6ef88bbf665e.png)


->List of songs followed by four buttons are displayed.
  1)A song can be selected from the list of songs(all song in your directory) are displayed and played using 'play' button.
  
  2)A song can be paused by using 'pause' button.
  
  3)Next song can be played using 'next' button.
  
  4)Prev song can be played using 'prev' button.
  
  5)The song which is being played is displayed at the botton of the window
  
  Output window:
  
  ![out_put_window](https://user-images.githubusercontent.com/26970266/37195822-617380b2-239a-11e8-957b-110c2b8bcf44.png)

Thanks
