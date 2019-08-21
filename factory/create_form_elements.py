from PyQt5 import QtWidgets
from PyQt5.QtCore import QFileInfo, pyqtSignal
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QHBoxLayout, QFileDialog


class CreateFormElements(QtWidgets.QWidget):
    filenameChanged = pyqtSignal(str)
    lineValueChanged = pyqtSignal(str)

    def __init__(self, label, fieldType, **kwargs):
        super(CreateFormElements, self)
        super().__init__()
        self.line_edit = QLineEdit()
        self.label = label
        self.fieldType = fieldType
        self.connectType = kwargs.get('connectType', None)
        self._fieldType = kwargs.get('_fieldType', None)
        self.create_form_row()

    def create_form_row(self):
        layout = QFormLayout()
        # if this is a button that should open up a file window, call the create_file_window() function to make a
        # file window.
        if self.connectType == 'file' and self._fieldType == 'button':
            self.fieldType.setText("Browse")
            self.fieldType.clicked.connect(self.create_file_window)
            hlayout = QHBoxLayout()
            hlayout.addWidget(self.line_edit)
            hlayout.addWidget(self.fieldType)
            layout.addRow(QLabel(self.label), hlayout)
        else:
            layout.addRow(QLabel(self.label), self.fieldType)

        self.get_data(self.fieldType)
        self.setLayout(layout)

    def create_file_window(self):
        fileName, _ = QFileDialog.getOpenFileName(None, 'Select Image', '', 'Image Files (*.png *.jpg '
                                                                            '*.jpeg *.bmp)')

        if fileName:
            self.line_edit.setText(fileName)
            self.filenameChanged.emit(fileName)
            from views.additem import AddNewItem
            AddNewItem.on_filename_changed(AddNewItem, fileName)

    def get_data(self, fieldType):
        objType = type(fieldType)

        if objType == QLineEdit:
            self.fieldType.textChanged.connect(self.get_text_val)

    def get_text_val(self, value):
        self.lineValueChanged.emit(value)
        from views.additem import AddNewItem
        AddNewItem.on_objectName_changed(AddNewItem, value)
