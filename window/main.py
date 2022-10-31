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
        self.username = ""
        self.password = ""
        
        if self.username and self.password:
            self.setLayout(self.mainPage())
        else:
            self.setLayout(self.loginPage())
            if self.username and self.password:
                self.setLayout(self.mainPage())
     
    def mainPage(self):
        mainLayout = QVBoxLayout()
        ecoButton = QPushButton('&Begin Eco-analysis', clicked=self.displayScore)
        mainLayout.addWidget(ecoButton)
        
        self.output = QTextEdit()
        mainLayout.addWidget(self.output)
        
        sendButton = QPushButton('&SendData', clicked=self.sendScore)
        mainLayout.addWidget(sendButton)
        return mainLayout
    
    def loginPage(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(250)
        self.input1.setFixedHeight(25)
        layout.addWidget(self.input1)
        
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(250)
        self.input2.setFixedHeight(25)
        layout.addWidget(self.input2)
 
        button = QPushButton("login")
        button.clicked.connect(self.setLoginInfo)
        button.clicked.connect(self.input1.clear)
        button.clicked.connect(self.input2.clear)
        button.clicked.connect(self.)
        #when button clicked check credentials
        #if credentials are good, then continue as usual
        layout.addWidget(button)
 
        
        # loginLayout = QVBoxLayout()
        
        # self.input1 = QLineEdit(self)
        # username = self.input1.text()
        
        
        # self.input2 = QLineEdit(self)
        # password = self.input2.text()
        
        # sendButton = QPushButton("&Login", clicked=self.setLoginInfo(username,password))
        
        # loginLayout.addWidget(self.input1)
        # loginLayout.addWidget(self.input2)
        # loginLayout.addWidget(sendButton)
        
        # return loginLayout
        return layout
    
    def setLoginInfo(self):
        self.username = self.input1.text()
        self.password = self.input2.text()
        print(self.username)
    
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
        Timer(5.0, self.sendScore).start()
        self.createState()
        #thread timer 5 minutes, generate json from current state object,
        # userData = user.user("Cristian", self.current.getEcoScore())
        # userJSON = json.dumps(userData.__dict__)
        # print(userJSON)
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