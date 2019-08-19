from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from lib.getConfig import load_config
import pathlib
import shutil


class AddNewItemController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.fileList = self._model.fname
        self.configs = load_config(self, 'settings/config.yml')
        self.assetDir = self.configs['imagespath']

    @pyqtSlot(str)
    def update_objName(self, value):
        self._model.myObjectName = value

    @pyqtSlot(list)
    def update_filename(self, value):
        self._model.fname.extend(value)

    def unique(self,data):
        return list(dict.fromkeys(data))

    def onSave(self):
        # prints to be removed
        # print(self._model.myObjectName)
        # print(self.fileList)
        # create a folder in the assets dir with the name of the object
        objectPath = self.assetDir + self._model.myObjectName
        pathlib.Path(objectPath).mkdir(exist_ok=True)

        # copy the selected files there and rename them
        fileList = self.unique(self._model.fname)
        for i in fileList:
            shutil.copy(i, objectPath)
