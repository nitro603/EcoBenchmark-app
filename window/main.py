from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from threading import Timer
from PyQt6.QtGui import QIcon
from monitor import getData
import sys
import json
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
        
        
    
    def createState(self):
        self.current = getData()
        userData = user.user("Cristian", self.current.getEcoScore())
        userJSON = json.dumps(userData.__dict__)
        print(userJSON)
        
    
    def displayScore(self):
        self.createState()
        outputText = self.current.getEcoScore()
        self.output.setText(outputText)
    
    def sendScore(self):
        #Timer(5.0, self.sendScore).start()
        self.createState()
        #thread timer 5 minutes, generate json from current state object,
        current = getData()
        userData = user.user("Cristian", self.current.getEcoScore())
        userJSON = json.dumps(userData.__dict__)
        
        print(userJSON)
        #uncomment the above code to send Json by button press and not automatically
        
        
        

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