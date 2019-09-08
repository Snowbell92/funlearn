import sys
from PyQt5.QtWidgets import QApplication
#from models.addNewItemModel import ModelAddNewItem
#from views.additem import AddNewItem
#from controller.addNewItemController import AddNewItemController
from views.showItem import ShowItem
from controller.showItemController import ShowItemController


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        #self.model = ModelAddNewItem()
        self.main_controller = ShowItemController()
        self.main_view = ShowItem(self.main_controller)
        self.main_view.show()



if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
