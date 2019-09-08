from pprint import pprint

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from factory.create_form_elements import CreateFormElements


# view
# Subclass QMainWindow to customise your application's main window
class AddNewItem(QMainWindow):
    objName = ''
    imageList = []

    def __init__(self, model, controller, *args, **kwargs):
        super(AddNewItem, self).__init__(*args, **kwargs)
        self._model = model
        self._controller = controller
        self.myWindow()

    def myWindow(self):
        self.setWindowTitle("Add New Item")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        # print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))
        self.width = 600
        self.height = 480
        self.left = 0
        self.top = 0
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setWindowState(QtCore.Qt.WindowMaximized)
        layout = QVBoxLayout()
        el_name = CreateFormElements("Object Name: ", QLineEdit())
        el_image = CreateFormElements("Add Images", None)
        el_image_1 = CreateFormElements("Image 1 ", QPushButton(), connectType='file', _fieldType='button')
        el_image_2 = CreateFormElements("Image 2 ", QPushButton(), connectType='file', _fieldType='button')
        el_image_3 = CreateFormElements("Image 1 ", QPushButton(), connectType='file', _fieldType='button')
        el_image_4 = CreateFormElements("Image 2 ", QPushButton(), connectType='file', _fieldType='button')
        el_save_button = QPushButton()
        el_save_button.setText('save')
        # this button is my save button
        self._model.fileName.connect(self.on_filename_changed)
        self._model.objName.connect(self.on_objectName_changed)
        el_save_button.clicked.connect(lambda n: self._controller.update_filename(self.imageList))
        el_save_button.clicked.connect(lambda x: self._controller.update_objName(self.objName))
        el_save_button.clicked.connect(self.saveItem)
        layout.addWidget(el_name)
        layout.addWidget(el_image)
        layout.addWidget(el_image_1)
        layout.addWidget(el_image_2)
        layout.addWidget(el_image_3)
        layout.addWidget(el_image_4)
        layout.addWidget(el_save_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def saveItem(self):
        isSaveSuccess = self._controller.onSave()
        if isSaveSuccess:
            self.showPopUp("Save Successful", "Item was added successfully!")
            # TODO: add buttons for either clearing the widgets or go back to prev screen
            for widget in QMainWindow.allWidgets():
                if isinstance(widget, QLineEdit):
                    print(widget)

    def showPopUp(self, title, message):
        QMessageBox.about(self, title, message)

    @pyqtSlot(list)
    def on_filename_changed(self, value):
        self.imageList.append(value)

    @pyqtSlot(str)
    def on_objectName_changed(self, value):
        self.objName = value
