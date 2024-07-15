import argparse
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui
from os import path
from PyQt5.QtCore import QUrl
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
# import playsound
import pygame
import qdarktheme



FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__), "gui.ui"))
class Main(QtWidgets.QMainWindow, FORM_CLASS):

    def __init__(self):
        super(Main,self).__init__()

        # Basic UI layout
        self.setupUi(self)
        self.translateButton.clicked.connect(self.translate)
        
        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("sound/007-2.mp3")
        
        # self.media_player = QMediaPlayer()
        # self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("sound/007.mp3")))
        # self.media_player.setVolume(50)
        

    def translate(self):
        english_text = self.mtayryEdit.toPlainText()
        arabic_text = self.english_to_arabic(english_text)
        self.textBrowser.clear()
        self.textBrowser.append(arabic_text)
        if(english_text=="" or arabic_text.isspace()):
            pass
        else:
            self.play_sound()
        
    def english_to_arabic(self, english_text):
        keyboard_mapping = {
            'q': 'ض',
            'w': 'ص',
            'e': 'ث',
            'r': 'ق',
            't': 'ف',
            'y': 'غ',
            'u': 'ع',
            'i': 'ه',
            'o': 'خ',
            'p': 'ح',
            '[': 'ج',
            ']': 'د',
            '\\': '\\',
            'a': 'ش',
            's': 'س',
            'd': 'ي',
            'f': 'ب',
            'g': 'ل',
            'h': 'ا',
            'j': 'ت',
            'k': 'ن',
            'l': 'م',
            ';': 'ك',
            '\'': 'ط',
            'z': 'ئ',
            'x': 'ء',
            'c': 'ؤ',
            'v': 'ر',
            'b': 'لا',
            'n': 'ى',
            'm': 'ة',
            ',': 'و',
            '.': 'ز',
            '/': 'ظ',
            'Q': 'َ',
            'W': 'ً',
            'E': 'ُ',
            'R': 'ٌ',
            'T': 'لإ',
            'Y': 'إ',
            'U': '‘',
            'I': '÷',
            'O': '×',
            'P': '؛',
            '{': '>',
            '}': '<',
            '|': '/',
            'A': 'ـ',
            'S': '،',
            'D': 'ْ',
            'F': 'ّ',
            'G': 'َّ',
            'H': 'ُّ',
            'J': 'ِّ',
            'K': 'ٍ',
            'L': 'لأ',
            ':': ':',
            '\"': '\"',
            'Z': 'َا',
            'X': 'ٰ',
            'C': 'آ',
            'V': 'أ',
            'B': 'إ',
            'N': '~',
            'M': 'ْ',
            '<': '.',
            '>': ',',
            '?': '؟'
        }
    
        # Map English letters to their equivalent Arabic letters using the keyboard mapping dictionary
        arabic_text = ''.join([keyboard_mapping.get(c, c) for c in english_text])
    
        return arabic_text  # To reverse the string to display it from right to left use [::-1]
    
    # def play_sound(self):
    #     self.media_player.setVolume(80) # set volume to 80%
    #     self.media_player.play()
    
    #     # create a QPropertyAnimation object that will gradually reduce the volume to 0 over 1 second
    #     animation = QPropertyAnimation(self.media_player, b"volume")
    #     animation.setDuration(3000) # 1 second
    #     animation.setStartValue(80) # start at 80%
    #     animation.setEndValue(0)   # end at 0%
    #     animation.setEasingCurve(QEasingCurve.OutQuad) # apply a quadratic easing curve to the animation
    #     animation.start()          # start the animation
    
    # def play_sound(self, sound_file_path):
    #     # set the volume to 0.5 (50%)
    #     volume = 0.5
    #     # play the sound effect
    #     playsound.playsound(sound_file_path, volume=volume, block=False)
    
    def play_sound(self):
        self.sound.stop()
        self.sound.set_volume(0.2)   # Now plays at 90% of full volume.
        self.sound.play() 
        self.sound.fadeout(25000) # 8000 is an ideal short version

    def closeEvent(self, event):
        # stop the sound effect when the window is closed
        self.sound.stop()
        event.accept()
        
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # qdarktheme.setup_theme(
    #     custom_colors={
    #         "[light]": {
    #             "background": "#3f4042",
    #         }
    #     }
    # )
    
    # not taking effect, preferred the light theme
    style = """
        QPlainTextEdit{
            font-size: 25px;
            }
        QTextBrowser{
            font-size: 25px;
            }
    """
    app.setStyleSheet(style)
    qdarktheme.setup_theme("light")
    mainwindow = Main()
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
# to run as a script
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Convert English text to Arabic text in the Arabic keyboard layout.')
#     parser.add_argument('text', type=str, help='the English text to convert')
#     args = parser.parse_args()

#     arabic_text = english_to_arabic_keyboard(args.text)
#     print(arabic_text)