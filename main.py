import sys

from PyQt6 import QtCore, QtMultimedia
from ui import Ui_MainWindow
from PyQt6.QtCore import Qt, QRectF, QPointF, QFile
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QLabel, QSlider

dict_filename = {
    'q': 'flute.mp3',
    'w': 'guitar.mp3',
    'e': 'bass.mp3',
    'r': 'clarinet.mp3',
    't': 'trombone.mp3',
}


class QTmusic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in self.playnotes.buttons():
            i.clicked.connect(self.btnPress)
        self.playmelody.clicked.connect(self.melody)

    def melody(self):
        for i in self.sender().text():
            self.play_sound(i)
            self._player.play()

    def btnPress(self):
        self.play_sound(self.sender().text())
        self._player.play()

    def keyPressEvent(self, event):
        self.button = ''
        if event.key() == Qt.Key.Key_Q:
            self.button = 'q'
        elif event.key() == Qt.Key.Key_W:
            self.button = 'w'
        elif event.key() == Qt.Key.Key_E:
            self.button = 'e'
        elif event.key() == Qt.Key.Key_R:
            self.button = 'r'
        elif event.key() == Qt.Key.Key_T:
            self.button = 't'
        if self.button:
            self.play_sound(self.button)

    def play_sound(self, button):
        filename = dict_filename[button]
        # print(filename)
        self._audio_output = QtMultimedia.QAudioOutput(self)
        self._audio_output.setVolume(50)
        self._player = QtMultimedia.QMediaPlayer(self)
        self._player.setAudioOutput(self._audio_output)
        self._player.setSource(QtCore.QUrl.fromLocalFile(filename))
        self._player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTmusic()
    ex.show()
    sys.exit(app.exec())
