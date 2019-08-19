from PyQt5.QtCore import QObject, pyqtSignal


class ModelAddNewItem(QObject):
    fileName = pyqtSignal(list)
    objName = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._flname = []
        self._myObjName = ''

    @property
    def fname(self):
        return self._flname

    @fname.setter
    def fname(self, value):
        self._flname = value
        self.fileName.emit(value)

    @property
    def myObjectName(self):
        return self._myObjName

    @myObjectName.setter
    def myObjectName(self, value):
        self._myObjName = value
        self.objName.emit(value)
