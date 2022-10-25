import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from random import randrange

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('EcoBenchmark')
        self.setWindowIcon(QIcon('earth.ico'))
        self.resize(600,350)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #widgets
        button = QPushButton('&Begin Eco-analysis', clicked=self.calculateEcoScore)
        self.output = QTextEdit()
        
        layout.addWidget(button)
        layout.addWidget(self.output)
    
    def calculateEcoScore(self):
        outputText = 'Computer Score is ' + str(randrange((100)))
        self.output.setText(outputText)

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