from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import * 


class GUIEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LKMK Editor")
        self.resize(600, 600)
        mainLayout = QVBoxLayout()
        titleContainer = QHBoxLayout()
        contentContainer = QHBoxLayout()
        row1 = QVBoxLayout()

        l = QTextItem("op")
        label1 = QLabel("LKMK Editor")
        label2 = QLabel("LKMK Editor")
        label3 = QLabel("LKMK Editor")

        btn1 = QPushButton("support")
        btn2 = QPushButton("support")
        btn3 = QPushButton("support")

        # Title Container:
        row1.addWidget(label1)
        row1.addWidget(label2)
        row1.addWidget(label3)
        
        # Content Container:
        row1.addWidget(btn1)
        row1.addWidget(btn2)
        row1.addWidget(btn3)

        # Layout Settings:
        contentContainer.addLayout(row1)
        mainLayout.addLayout(titleContainer)
        mainLayout.addLayout(contentContainer)

        # View Init:
        self.setLayout(mainLayout)
        self.show()

    

    def initGUI(self):
        pass
        #app Setup:
        # app = QApplication([])
        # app.setStyle('macos')
        # window = QMainWindow()
        # window.setWindowTitle("hello")

        # # layouts:
        # v_layout = QVBoxLayout()
        # h_layout = QHBoxLayout()
        
       
        
        # # groupbox layout:
        # groupBox = QGroupBox("Test Example")
        # testlayout = QHBoxLayout()
        # groupBox.setLayout(testlayout)

        # # Dropdown Menu Widget
        # dropDown = QComboBox()
        # dropDown.addItems(['One', 'Two', 'Three', 'Four'])
        # v_layout.addWidget(groupBox)
        # v_layout.addWidget(QLabel('hello world'))
        # v_layout.addWidget(dropDown)
        # # v_layout.addWidget(btn1)
        # # v_layout.addWidget(btn2)

        # # adding and setting up adn executing the layouts:
        # h_layout.addLayout(v_layout)
        # window.setLayout(h_layout)
        # window.show()
        # app.exec()

        #### Tray Icon Start ####
            # tray = QSystemTrayIcon()
            # tray.setVisible(True)

            # statusBarMenu = QMenu()
            # action = QAction("A menu item")
            # statusBarMenu.addAction(action)

            # quit = QAction("Quit")
            # quit.triggered.connect(app.quit)
            # statusBarMenu.addAction(quit)

            # tray.setContextMenu(statusBarMenu)
        #### Tray Icon End ###