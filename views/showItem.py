import sys
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QPushButton


class ShowItem(QMainWindow):
    def __init__(self, controller, *args, **kwargs):
        super(ShowItem, self).__init__(*args, **kwargs)
        self._controller = controller
        self.counter = 0
        self.showWindow()

    def showWindow(self):
        self.setWindowTitle("You are learning")
        self.width = 600
        self.height = 480
        self.left = 0
        self.top = 0
        self.setGeometry(self.left, self.top, self.width, self.height)
        el_next_item = QPushButton()
        el_next_item.setText('Next Item')
        imageFiles = self._controller.getItem(self.counter)
        print(imageFiles)
        el_next_item.clicked.connect(self.increaseCounter)
        layout = QVBoxLayout()
        widget = QWidget()
        layout.addWidget(el_next_item)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def increaseCounter(self):
        self.counter += 1
