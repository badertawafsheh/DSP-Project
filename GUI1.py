import winsound
import numpy as np
import matplotlib.pyplot as plt
import playsound as playsound
import wavio as wavio
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)

        MainWindow.setStyleSheet("color :rgb(6, 6, 6)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(71, 214, 171, 42))
        self.label.setMinimumSize(QtCore.QSize(5, 3))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(8, 0))
        self.label.setBaseSize(QtCore.QSize(5, 8))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Painter")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/play_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(23, 31))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Painter")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/statistics_filled_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 220, 411, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 90, 101, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./images/rfid_signal_100px.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.startProgram)
        self.pushButton.clicked.connect(self.playSoundP)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DSP Phase 1 "))
        self.label.setText(_translate("MainWindow", "Enter The String :"))
        self.pushButton.setText(_translate("MainWindow", "PLAY"))
        self.pushButton_2.setText(_translate("MainWindow", "Draw"))

    def startProgram(self):
        Chars = [{'a': '400', 'b': '400', 'c': '400', 'd': '400', 'e': '400', 'f': '400', 'g': '400', 'h': '400',
                  'i': '400', 'j': '600', 'k': '600', 'l': '600', 'm': '600', 'n': '600', 'o': '600', 'p': '600',
                  'q': '600', 'r': '600', 's': '800', 't': '800', 'u': '800', 'v': '800', 'w': '800', 'x': '800',
                  'y': '800', 'z': '800', ' ': '800', },
                 {'a': '1000', 'b': '1000', 'c': '1000', 'd': '1200', 'e': '1200', 'f': '1200', 'g': '1500',
                  'h': '1500',
                  'i': '1500', 'j': '1000', 'k': '1000', 'l': '1000', 'm': '1200', 'n': '1200', 'o': '1200',
                  'p': '1500',
                  'q': '1500', 'r': '1500', 's': '1000', 't': '1000', 'u': '1000', 'v': '1200', 'w': '1200',
                  'x': '1200',
                  'y': '1500', 'z': '1500', ' ': '1500', },
                 {'a': '2000', 'b': '3000', 'c': '4000', 'd': '2000', 'e': '3000', 'f': '4000', 'g': '2000',
                  'h': '3000',
                  'i': '4000', 'j': '2000', 'k': '3000', 'l': '4000', 'm': '2000', 'n': '3000', 'o': '4000',
                  'p': '2000',
                  'q': '3000', 'r': '4000', 's': '2000', 't': '3000', 'u': '4000', 'v': '2000', 'w': '3000',
                  'x': '4000',
                  'y': '2000', 'z': '3000', ' ': '4000', }]
        string = self.textEdit.toPlainText()
        y = self.encode(string, Chars)
        self.wave(y, "DSP.wav")
        plt.plot(y[:100])
        plt.suptitle('Signal For String')
        plt.gcf().canvas.set_window_title('DSP PHASE 1')
        plt.show()

    def encode(self, string, chars):
        fs = 44000
        T = 0.04
        n = np.arange(0, fs * T, 1)
        string = string.lower()
        string = list(string)
        y = []
        for i in range(0, len(string)):
            x = np.cos(2 * np.pi * int(chars[0][string[i]]) * n / fs)
            x += np.cos(2 * np.pi * int(chars[1][string[i]]) * n / fs)
            x += +np.cos(2 * np.pi * int(chars[2][string[i]]) * n / fs)
            y = np.concatenate([y, x])
        return y

    def wave(self, y, file_name):
        length = len(y)
        wavio.write(file_name, y, length, sampwidth=1)
    def playSoundP(self):
        winsound.PlaySound("DSP.wav", winsound.SND_FILENAME)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
