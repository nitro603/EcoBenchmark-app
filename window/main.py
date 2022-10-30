import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from random import randrange
from monitor import getData

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
        
        sendButton = QPushButton('&SendData', clicked=self.displayScore)
        layout.addWidget(sendButton)
    
    def displayScore(self):
        current = getData()
        outputText = current.getEcoScore()
    
        self.output.setText(outputText)
        
    #def sendScore(self):
        
        #userJSON = json.dumps
        
        

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