from PyQt5.QtCore import QObject
from factory.getConfig import load_yaml_file
import pathlib


class ShowItemController(QObject):
    def __init__(self):
        super().__init__()
        self.objectList = load_yaml_file(self, 'files/object.yaml')
        self.configs = load_yaml_file(self, 'settings/config.yml')
        self.assetDir = self.configs['imagespath']

    def getItem(self, counter):
        itemCount = len(self.objectList['objects'])
        i = counter
        if counter > itemCount:
            i = 0
        currentItem = self.objectList['objects'][i]
        path = pathlib.Path(self.assetDir + currentItem)
        files = [str(e) for e in path.iterdir() if e.is_file()]
        return files


