import os

import yaml
from PyQt5.QtCore import QObject, pyqtSlot
from factory.getConfig import load_yaml_file
import pathlib
import shutil


def findFiles(directory):
    fileList = []
    iterator = directory.iterdir()
    for entry in iterator:
        if entry.is_file():
            entryPath = entry.parent / entry.name
            fileList.append(entryPath)

    return fileList


def unique(data):
    return list(dict.fromkeys(data))


class AddNewItemController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.fileList = self._model.fname
        self.configs = load_yaml_file(self, 'settings/config.yml')
        self.assetDir = self.configs['imagespath']

    @pyqtSlot(str)
    def update_objName(self, value):
        self._model.myObjectName = value

    @pyqtSlot(list)
    def update_filename(self, value):
        self._model.fname.extend(value)

    def onSave(self):
        # create a folder in the assets dir with the name of the object
        objectPath = self.assetDir + self._model.myObjectName
        pathlib.Path(objectPath).mkdir(exist_ok=True)

        # copy the selected files there and rename them
        fileList = unique(self._model.fname)
        for i in fileList:
            shutil.copy(i, objectPath)

        # get new image path after copy
        imgList = findFiles(pathlib.Path(objectPath))

        # rename the copied files
        # TODO: duplicate file rename error handling
        for f in imgList:
            currentDir = pathlib.Path(objectPath)
            img = pathlib.Path(f)
            imgExt = img.suffix
            index = str((imgList.index(f)) + 1)
            imgName = "_".join([self._model.myObjectName, index])
            img.rename(os.path.join(currentDir, (imgName + imgExt)))

        # save the name of the object in the objects.yaml file
        with open('files/object.yaml', 'r') as yamlfile:
            try:
                cur_yaml = yaml.safe_load(yamlfile)
                if cur_yaml['objects'] is None:
                    cur_yaml['objects'] = []
                cur_yaml["objects"].append(str(self._model.myObjectName))
                print(cur_yaml)
            except yaml.YAMLError as exception:
                print(exception)
                return False

        with open('files/object.yaml', 'w') as yamlfile:
            try:
                yaml.safe_dump(cur_yaml, yamlfile, explicit_start=True, allow_unicode=True, encoding='utf-8')
            except yaml.YAMLError as exception:
                print(exception)
                return False

        # TODO: handle file errors.
        return True
