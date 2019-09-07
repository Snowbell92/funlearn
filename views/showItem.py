import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QPushButton, QLabel


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
        # image slideshow. it will not play on it it's own
        imageFiles = self._controller.getItem(self.counter)
        el_pic_label= QLabel(self)
        el_pixmap = QPixmap(imageFiles[0])
        el_pic_label.setPixmap(el_pixmap)
        el_next_item.clicked.connect(self.increaseCounter)
        layout = QVBoxLayout()
        widget = QWidget()
        layout.addWidget(el_pic_label)
        layout.addWidget(el_next_item)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def increaseCounter(self):
        self.counter += 1
