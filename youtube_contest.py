from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os

song = []


pygame.init()
volume = 0.5
def open_file():
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    print(song)
    ui.list.addItems(song)

def play():
    i = ui.list.currentRow()
    melody = ui.list.item(i).text()
    pygame.mixer.music.load( melody )
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()


def volume_up():
    global volume
    if volume < 0.9 :
        volume += 0.1
        ui.label_2.setText( str(round(volume*100))+ '%' )
        pygame.mixer.music.set_volume(volume)

def volume_down():
    global volume
    if volume > 0.1 :
        volume -= 0.1
        ui.label_2.setText(str(round(volume*100)) + '%' )
        pygame.mixer.music.set_volume(volume)

def find_files():
    global song
    dir = QFileDialog.getExistingDirectory()
    print(dir)
    for d , dn , fs in os.walk(dir):
        for f in fs:
            if '.mp3' in f:
                file = os.path.join(d, f)
                song.append(file)
    print(song)
    ui.list.addItems(song)
     

def clear1():
    global song
    song = []
    ui.list.clear()


def save_playlist():
    global song
    import pickle
    f = open('playlist.dat', 'wb')
    pickle.dump(song, f)
    f.close()

def load_playlist():
    global song
    import pickle
    f = open('playlist.dat', 'rb')
    song = pickle.load(f)
    ui.list.addItems(song)  

def pause():
    pygame.mixer.music.pause()


def continue_2():
    pygame.mixer.music.unpause()

app = QApplication([])
ui = uic.loadUi("mmmp3.html")


ui.show()
ui.btn1.clicked.connect(open_file)
ui.btn2.clicked.connect(play)
ui.btn3.clicked.connect(stop)

ui.pushButton.clicked.connect(volume_up)
ui.pushButton_2.clicked.connect(volume_down)


ui.find.clicked.connect(find_files)

ui.pushButton_3.clicked.connect(clear1)
ui.pushButton_4.clicked.connect(load_playlist)
ui.pushButton_5.clicked.connect(save_playlist)

ui.btn4.clicked.connect(pause)

ui.pushButton_6.clicked.connect(continue_2)

app.exec_()