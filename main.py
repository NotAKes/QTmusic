import sys

from PyQt6 import QtCore, QtMultimedia
from ui import Ui_MainWindow
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QLabel, QSlider

dict_filename = {
    'q': 'media/flute.mp3',
    'w': '',
    'e': '',
    'r': '',
    't': '',
}


class QTmusic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in self.playnotes.buttons():
            i.clicked.connect(self.btnPress)

    def btnPress(self):
        self.play_sound(self.sender().text())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.button = 'q'
        if event.key() == Qt.Key.Key_W:
            self.button = 'w'
        if event.key() == Qt.Key.Key_E:
            self.button = 'e'
        if event.key() == Qt.Key.Key_R:
            self.button = 'r'
        if event.key() == Qt.Key.Key_T:
            self.button = 't'
        self.play_sound(self.button)

    def play_sound(self, button):
        print(button)
        media = QtCore.QUrl.fromLocalFile(dict_filename[button])
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTmusic()
    ex.show()
    sys.exit(app.exec())
