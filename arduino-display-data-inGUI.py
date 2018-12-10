import serial
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

arduinoData = serial.Serial('COM3',9600,timeout = 2)

class appArduino(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400,250,600,400)
        self.setWindowTitle('Random Values From Serial Port')
        self.setWindowIcon(QIcon('myIcon.png'))
        
        label = QLabel(self)
        label.setText('Random values')
        label.setGeometry(270,50,200,75)

        display = QTextEdit(self)
        display.setGeometry(150,100,300,100)
        display.setReadOnly(True)

        button = QPushButton('Quit',self)
        button.setGeometry(280,220,60,30)
        button.clicked.connect(QCoreApplication.instance().quit)

        i=0
        while i<8:
        
           if(arduinoData.inWaiting()>0):
                data = arduinoData.readline().decode('ascii')    # using decode to remove the \n\r characters
                i = i+1
                display.append(data)
                
        self.show()

if __name__ == '__main__':
    
    app  = QApplication(sys.argv)   #creating an application object
    window = appArduino()   
    sys.exit(app.exec_())
