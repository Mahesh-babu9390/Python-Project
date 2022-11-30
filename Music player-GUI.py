from tkinter import * #import tkinter to create gui applications
from tkinter import filedialog #To get and helps to open the files from system
from pygame import mixer #To designs the sound libraries in graphics
#creating a class
class MusicPlayer:
 # defing the paramatrized constructor
 def __init__(self, window):
 window.geometry('320x100'); #size of the window
 window.title('groove music'); #title of music player
 window.resizable(0, 0)
 #load button
 Load = Button(window, text='Load', width=10, font=('Times', 10),
command=self.load)
 #play button
 Play = Button(window, text='Play', width=10, font=('Times', 10),
command=self.play)
 #pause button
 Pause = Button(window, text='Pause', width=10, font=('Times', 10),
command=self.pause)
 #stop button
 Stop = Button(window, text='Stop', width=10, font=('Times', 10),
command=self.stop)
 Load.place(x=0, y=20);
 Play.place(x=110, y=20);
 Pause.place(x=220, y=20); #size and position of the buttons
 Stop.place(x=110, y=60)
 self.music_file = False
 self.playing_state = False
 #adding songs from files
 def load(self):
 self.music_file = filedialog.askopenfilename()
 #To play the song
 def play(self):
 if self.music_file:
 mixer.init()
 mixer.music.load(self.music_file)
 mixer.music.play()
 #To pause the song
 def pause(self):
 if not self.playing_state:
 mixer.music.pause()
 self.playing_state = True
 else:
 mixer.music.unpause()
 self.playing_state = False
 #To stop the song
 def stop(self):
 mixer.music.stop()
#menu
root = Tk()
app = MusicPlayer(root)
root.mainloop()