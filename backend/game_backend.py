# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\backend\additem2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1960, 1420)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QtGui.QColor(235, 255, 211))
        Form.setPalette(p)

        self.label= QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 30, 700, 50))
        self.label.setText("Add image parts for game module")
        self.label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Black))


        self.label1= QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(350, 100, 400, 70))
        self.label1.setText("Select image part 1 ")
        self.label1.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        self.vidlineEdit = QtWidgets.QLineEdit(Form)
        self.vidlineEdit.setGeometry(QtCore.QRect(150, 150, 550, 40))
        self.vidlineEdit.setObjectName("vidlineEdit")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(370,210,93,28))
        self.vidpushButton.setObjectName("vidpushButton")
        

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(1100, 100, 361, 70))
        self.label2.setText("Select image part 2 ")
        self.label2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit = QtWidgets.QLineEdit(Form)
        self.imglineEdit.setGeometry(QtCore.QRect(880, 150, 550, 40))
        self.imglineEdit.setObjectName("imglineEdit")
        self.imgpushButton1 = QtWidgets.QPushButton(Form)
        self.imgpushButton1.setGeometry(QtCore.QRect(1100, 210, 93, 28))
        self.imgpushButton1.setObjectName("imgpushButton1")

        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(350, 250, 361, 70))
        self.label3.setText("Select image part 3 ")
        self.label3.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit2 = QtWidgets.QLineEdit(Form)
        self.imglineEdit2.setGeometry(QtCore.QRect(150, 300, 550, 40))
        self.imglineEdit2.setObjectName("imglineEdit")
        self.imgpushButton2 = QtWidgets.QPushButton(Form)
        self.imgpushButton2.setGeometry(QtCore.QRect(370, 360, 93, 28))
        self.imgpushButton2.setObjectName("imgpushButton2")


        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(1100, 250, 361, 70))
        self.label4.setText("Select image part 4 ")
        self.label4.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit3 = QtWidgets.QLineEdit(Form)
        self.imglineEdit3.setGeometry(QtCore.QRect(880, 300,550, 40))
        self.imglineEdit3.setObjectName("imglineEdit")
        self.imgpushButton3 = QtWidgets.QPushButton(Form)
        self.imgpushButton3.setGeometry(QtCore.QRect(1120, 360, 93, 28))
        self.imgpushButton3.setObjectName("imgpushButton3")

        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(350, 400, 361, 70))
        self.label5.setText("Select full image ")
        self.label5.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(150, 450, 550, 40))
        self.addName.setObjectName("addName")
        self.addNameButton=QtWidgets.QPushButton(Form)
        self.addNameButton.setGeometry(QtCore.QRect(370,520,150,28))
        self.addNameButton.setObjectName("addNameButton")

        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(1050, 450, 311, 61))
        self.objpushButton.setObjectName("objpushButton")
        

        self.addNameButton.clicked.connect(self.setImage1)
        self.imgpushButton1.clicked.connect(self.setImage2)
        self.imgpushButton2.clicked.connect(self.setImage3)
        self.imgpushButton3.clicked.connect(self.setImage4)
        self.vidpushButton.clicked.connect(self.setImage5)
        self.objpushButton.clicked.connect(self.additem)
        

        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addNameButton.setText(_translate("Form","Add full image"))
        self.vidpushButton.setText(_translate("Form", "Add Image"))
        self.imgpushButton1.setText(_translate("Form", "Add Image"))
        self.imgpushButton2.setText(_translate("Form", "Add Image"))
        self.imgpushButton3.setText(_translate("Form", "Add Image"))
        self.objpushButton.setText(_translate("Form", "Add Object"))
        

    def setImage1(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/assets/gamepic", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.addName.setText(ifileName)
    def setImage2(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/assets/gamepic", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit.setText(ifileName)
    def setImage3(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/assets/gamepic", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit2.setText(ifileName)
    def setImage4(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/assets/gamepic", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit3.setText(ifileName)

    def setImage5(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/assets/gamepic", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.vidlineEdit.setText(ifileName)


    

    def deleting(self):
        #self.imgLabel.clear()
        self.imglineEdit.setText("")
        self.imglineEdit2.setText("")
        self.imglineEdit3.setText("")
        #self.VideoLabel.clear()
        self.vidlineEdit.setText("")
        
        self.addName.setText("")

    def additem(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        ifileName1=self.imglineEdit.text();
        ifileName2=self.imglineEdit2.text();
        ifileName3=self.imglineEdit3.text();
        print(ifileName2)
        vfileName=self.vidlineEdit.text();
        
        name=self.addName.text()
        myCursor = mydb.cursor()
        
        
        sql = "INSERT INTO game(main_image,image_name_1, image_name_2, image_name_3, image_name_4 ) VALUES(%s, %s, %s, %s, %s)"
        val = (name,vfileName,ifileName1,ifileName2,ifileName3 ) 
        print(name)
        
        myCursor.execute(sql, val)
        mydb.commit()
        myCursor.close()
        mydb.close()

        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Item")
        messageBox.setText("Item added!")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
        self.deleting()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

