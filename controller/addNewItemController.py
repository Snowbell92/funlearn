from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from lib.getConfig import load_config


class AddNewItemController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.fileList = self._model.fname

    @pyqtSlot(str)
    def update_objName(self, value):
        self._model.myObjectName = value

    @pyqtSlot(list)
    def update_filename(self, value):
        self._model.fname.extend(value)

    def onSave(self):
        print(self._model.myObjectName)
        print(self.fileList)
