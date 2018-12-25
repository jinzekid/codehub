# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

from SetTaskDetail import *
from TaskManager import *

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_QDSetTaskDetail()
        self.child.setupUi(self)
        self.child.initUIAction()

    """对QDialog类重写，实现一些功能"""
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """

        if self.child.finish_set():
            event.accept()
        else:
            reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否取消任务设置？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def close_dialog(self):
        self.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 85, 801, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ListOfTask = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ListOfTask.setObjectName("ListOfTask")
        self.gridLayout.addWidget(self.ListOfTask, 2, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 781, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddNewTask = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddNewTask.sizePolicy().hasHeightForWidth())
        self.btnAddNewTask.setSizePolicy(sizePolicy)
        self.btnAddNewTask.setObjectName("btnAddNewTask")
        self.horizontalLayout_2.addWidget(self.btnAddNewTask)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ui_set_task_detail = childWindow()
        #  初始化全局任务管理器
        TaskManager().init_taskManager()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "任务列表："))
        self.btnAddNewTask.setText(_translate("MainWindow", "新增任务"))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.actiondakai.setText(_translate("MainWindow", "dakai "))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))

    def initUIAction(self):
        self.btnAddNewTask.clicked.connect(self.show_set_new_task_detail)

    def show_set_new_task_detail(self):
        '''
        显示任务详情界面
        :return:
        '''
        self.ui_set_task_detail.child.init_task_detail_info(self.refresh_list_of_tasks)
        self.ui_set_task_detail.setModal(True)
        self.ui_set_task_detail.show()

    def refresh_list_of_tasks(self, newTask):
        print("task name: " + newTask.name)

        item = QtWidgets.QListWidgetItem(QIcon("img/icon-prompt.png"), newTask.name)
        self.ListOfTask.addItem(item)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initUIAction()
    MainWindow.show()
    sys.exit(app.exec_())

