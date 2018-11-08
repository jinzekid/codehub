# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QDialog
from PyQt5.QtWidgets import QFileDialog

from SetTaskDetail import *
import LYUtils as utils

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_QDSetTaskDetail()
        self.child.setupUi(self)
        self.child.initUIAction()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.sourceOfFiles = []
        self.ui_set_task_detail = childWindow()
        self.dt = 0
        self.timer = QTimer()

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
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 20))
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
        self.labFromPath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labFromPath.setText("")
        self.labFromPath.setObjectName("labFromPath")
        self.gridLayout.addWidget(self.labFromPath, 2, 0, 1, 1)
        self.ListOfSourceFiles = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ListOfSourceFiles.setObjectName("ListOfSourceFiles")
        self.gridLayout.addWidget(self.ListOfSourceFiles, 3, 0, 1, 1)
        self.btnChooseFromPath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnChooseFromPath.setObjectName("btnChooseFromPath")
        self.gridLayout.addWidget(self.btnChooseFromPath, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.BtnAddFiles = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BtnAddFiles.setObjectName("BtnAddFiles")
        self.verticalLayout.addWidget(self.BtnAddFiles)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnChooseToPath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnChooseToPath.setObjectName("btnChooseToPath")
        self.gridLayout_2.addWidget(self.btnChooseToPath, 0, 0, 1, 1)
        self.labToPath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labToPath.setText("")
        self.labToPath.setObjectName("labToPath")
        self.gridLayout_2.addWidget(self.labToPath, 1, 0, 1, 1)
        self.ListOfDestinationFiles = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ListOfDestinationFiles.setObjectName("ListOfDestinationFiles")
        self.gridLayout_2.addWidget(self.ListOfDestinationFiles, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
        self.btnSetTask = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnSetTask.setObjectName("btnSetTask")
        self.horizontalLayout_2.addWidget(self.btnSetTask)
        self.btnFinishSet = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnFinishSet.setObjectName("btnFinishSet")
        self.horizontalLayout_2.addWidget(self.btnFinishSet)
        self.dateObj = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateObj.setObjectName("dateObj")
        self.horizontalLayout_2.addWidget(self.dateObj)
        self.labCntTime = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labCntTime.setObjectName("labCntTime")
        self.horizontalLayout_2.addWidget(self.labCntTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnChooseFromPath.setText(_translate("MainWindow", "源目录"))
        self.BtnAddFiles.setText(_translate("MainWindow", "添加"))
        self.btnChooseToPath.setText(_translate("MainWindow", "目标目录"))
        self.btnSetTask.setText(_translate("MainWindow", "设置任务"))
        self.btnFinishSet.setText(_translate("MainWindow", "完成设置"))
        self.labCntTime.setText(_translate("MainWindow", "00:00:00"))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.actiondakai.setText(_translate("MainWindow", "dakai "))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))

    def initUIAction(self):
        self.btnChooseFromPath.clicked.connect(self.do_choose_directory)
        self.btnSetTask.clicked.connect(self.show_task_detail)
        self.btnFinishSet.clicked.connect(self.do_finish_set_task)

        # 设置日期编辑器格式
        self.dateObj.setDateTime(QDateTime.currentDateTime())
        self.dateObj.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateObj.setCalendarPopup(True) # 设置日历空间允许弹出


        # 设置list的选择模式为多选
        self.ListOfSourceFiles.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        # 设置list的选项动作
        self.ListOfSourceFiles.itemClicked.connect(self.do_source_item_clicked)

    def do_finish_set_task(self):
        print(self.dateObj.text())
        print(self.dateObj.dateTime())
        taskQDateTime = int(self.dateObj.dateTime().toTime_t())
        print("task time:" + str(taskQDateTime))
        curTime = int(time.time()) #获取时间戳
        print("cur time:" + str(curTime))

        self.dt = taskQDateTime - curTime
        print("dt:" + (utils.format_time(self.dt)))

        # 开始倒计时
        self.init_count_down_timer(self.timer)
        self.refresh_count_down()

    def init_count_down_timer(self, timer):
        timer.setInterval(1000)
        timer.timeout.connect(self.refresh_count_down)
        timer.start()
        return timer

    def refresh_count_down(self):
        if self.dt > 0:
            self.labCntTime.setText((utils.format_time(self.dt)))
            self.dt -= 1
        else:
            self.labCntTime.setText('00:00:00')
            self.dt = 0
            self.timer.stop()
        pass

    def show_task_detail(self):
        self.ui_set_task_detail.setModal(True)
        self.ui_set_task_detail.show()

    def do_source_item_clicked(self):
        print(self.ListOfSourceFiles.currentItem())
        indexs = self.ListOfSourceFiles.selectedIndexes()
        items = self.ListOfSourceFiles.selectedItems()
        print(indexs)
        for item in items:
            print(item.text())

    def do_choose_directory(self):
        directory1 = QFileDialog.getExistingDirectory(self.centralwidget,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        print(directory1)

        self.labFromPath.setText(directory1)

        self.update_directory_files(directory1)

        """
        files, ok1 = QFileDialog.getOpenFileNames(self.centralwidget,
                                                  "多文件选择", "./",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files, ok1)
        self.sourceOfFiles = files
        self.ListOfSourceFiles.addItems(self.sourceOfFiles)
        """

    def update_directory_files(self, directory):
        rootdir = directory
        list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件

        self.ListOfSourceFiles.addItems(list)
        """
        for i in range(0, len(list)):
            #path = os.path.join(rootdir, list[i])
            print("file name" , type(list[i]))
            self.ListOfSourceFiles.addItems(list[i]))
        """

    # 删除指定文件
    def do_del_file(self, idx):
        if len(self.listOfSourceFiles) > 0 and idx >= 0:
            delFileName = self.listOfSourceFiles.pop(idx)
            print('>>:del file name:' + delFileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initUIAction()
    MainWindow.show()
    sys.exit(app.exec_())