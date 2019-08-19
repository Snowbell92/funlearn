import sys
from PyQt5.QtWidgets import QApplication
from models.addNewItemModel import ModelAddNewItem
from views.additem import AddNewItem
from controller.addNewItemController import AddNewItemController


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ModelAddNewItem()
        self.main_controller = AddNewItemController(self.model)
        self.main_view = AddNewItem(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
