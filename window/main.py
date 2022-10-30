from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from random import randrange
from monitor import getData
import sys
import json
import threading
import user


class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('EcoBenchmark')
        self.setWindowIcon(QIcon('earth.ico'))
        self.resize(600,350)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #widgets
        ecoButton = QPushButton('&Begin Eco-analysis', clicked=self.displayScore)
        self.output = QTextEdit()
        
        layout.addWidget(ecoButton)
        layout.addWidget(self.output)
        
        sendButton = QPushButton('&SendData', clicked=self.sendScore)
        layout.addWidget(sendButton)
    
    def displayScore(self):
        current = getData()
        outputText = current.getEcoScore()
    
        self.output.setText(outputText)
        
    def sendScore(self):
        #threading.Timer(20.0, getData).start()
        #thread timer 5 minutes, generate json from current state object, :)))
        current = getData()
        userData = user.user("Cristian", current.getEcoScore())
        userJSON = json.dumps(userData.__dict__)
        print(userJSON)
        
        

#only used when you run the application from a command prompt
#later you'll have to change this
app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }              
    
    QPushButton {
        font-size: 20px
    }
                  
    ''')

window = MyApp()
window.show()

app.exec()