# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetTaskDetail.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import time
import shutil

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QDialog
from PyQt5.QtWidgets import QFileDialog

import LYUtils as utils
from MyTask import *
from TaskManager import *

class Ui_QDSetTaskDetail(object):
    def setupUi(self, QDSetTaskDetail):

        self.dialog = QDSetTaskDetail

        QDSetTaskDetail.setObjectName("QDSetTaskDetail")
        QDSetTaskDetail.resize(716, 560)
        self.horizontalLayoutWidget = QtWidgets.QWidget(QDSetTaskDetail)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 691, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labSrcPath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labSrcPath.sizePolicy().hasHeightForWidth())
        self.labSrcPath.setSizePolicy(sizePolicy)
        self.labSrcPath.setText("")
        self.labSrcPath.setObjectName("labSrcPath")
        self.gridLayout_3.addWidget(self.labSrcPath, 1, 0, 1, 1)
        self.btnChooseFromPath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnChooseFromPath.setObjectName("btnChooseFromPath")
        self.gridLayout_3.addWidget(self.btnChooseFromPath, 0, 0, 1, 1)
        self.listWidgetOfSrc = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidgetOfSrc.setObjectName("listWidgetOfSrc")
        self.gridLayout_3.addWidget(self.listWidgetOfSrc, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.BtnAddFiles = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BtnAddFiles.setObjectName("BtnAddFiles")
        self.verticalLayout.addWidget(self.BtnAddFiles)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labDestPath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labDestPath.sizePolicy().hasHeightForWidth())
        self.labDestPath.setSizePolicy(sizePolicy)
        self.labDestPath.setText("")
        self.labDestPath.setObjectName("labDestPath")
        self.gridLayout_4.addWidget(self.labDestPath, 1, 0, 1, 1)
        self.btnChooseToPath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChooseToPath.sizePolicy().hasHeightForWidth())
        self.btnChooseToPath.setSizePolicy(sizePolicy)
        self.btnChooseToPath.setObjectName("btnChooseToPath")
        self.gridLayout_4.addWidget(self.btnChooseToPath, 0, 0, 1, 1)
        self.listWidgetOfDest = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidgetOfDest.setObjectName("listWidgetOfDest")
        self.gridLayout_4.addWidget(self.listWidgetOfDest, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(QDSetTaskDetail)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(540, 20, 160, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnOK = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_3.addWidget(self.btnOK)
        self.btnCancle = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancle.sizePolicy().hasHeightForWidth())
        self.btnCancle.setSizePolicy(sizePolicy)
        self.btnCancle.setObjectName("btnCancle")
        self.horizontalLayout_3.addWidget(self.btnCancle)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(QDSetTaskDetail)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 430, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.TaskOfName = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskOfName.sizePolicy().hasHeightForWidth())
        self.TaskOfName.setSizePolicy(sizePolicy)
        self.TaskOfName.setObjectName("TaskOfName")
        self.verticalLayout_3.addWidget(self.TaskOfName)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.objDateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.objDateTimeEdit.setSizePolicy(sizePolicy)
        self.objDateTimeEdit.setObjectName("objDateTimeEdit")
        self.verticalLayout_2.addWidget(self.objDateTimeEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(QDSetTaskDetail)
        QtCore.QMetaObject.connectSlotsByName(QDSetTaskDetail)

        self.taskManager = TaskManager()
        self.__init_properties()

    def retranslateUi(self, QDSetTaskDetail):
        _translate = QtCore.QCoreApplication.translate
        QDSetTaskDetail.setWindowTitle(_translate("QDSetTaskDetail", "Dialog"))
        self.btnChooseFromPath.setText(_translate("QDSetTaskDetail", "源目录"))
        self.BtnAddFiles.setText(_translate("QDSetTaskDetail", "添加"))
        self.btnChooseToPath.setText(_translate("QDSetTaskDetail", "目标目录"))
        self.btnOK.setText(_translate("QDSetTaskDetail", "确定"))
        self.btnCancle.setText(_translate("QDSetTaskDetail", "取消"))
        self.label_2.setText(_translate("QDSetTaskDetail", "任务名称:"))
        self.label.setText(_translate("QDSetTaskDetail", "设置时间:"))

    def __init_properties(self):
        self.srcDir = ''
        self.destDir = ''
        self.srcPath = ''
        self.destPath = ''
        self.dt = 0
        self.selectedItems = []
        self.sourceOfFiles = []
        self.destOfFiles = []
        self.__finishToSet = False
        self.after_add_task = None

        self.TaskOfName.setPlaceholderText("任务名称")

        # def set_finish_add_task_cbFunc(self, finishFunc):
        #    self.cbFinishFunc = finishFunc

    def new_task_detail(self, refresh_task):
        self.__finish_to_set = False
        self.__init_properties()
        self.after_add_task = refresh_task

    def init_task_detail_info(self, task):
        print('init task detail info:' + task.name)
        self.__finish_to_set = False
        self.__init_properties()
        #self.after_add_task = func_refresh_tasks

        # 设置任务名称
        self.TaskOfName.setText(task.name)
        self.__init_src_dir(task.srcPath)
        self.__init_dest_dir(task.destPath)

        # 设置任务的中被选中的文件
        listOfFiles = []
        for selectedFile in task.srcOfFiles:
            listOfFiles.append(selectedFile)

        count = self.listWidgetOfSrc.count()
        for row in range(count):
            item = self.listWidgetOfSrc.item(row)
            for i in range(len(listOfFiles)-1, -1, -1):
                selectedFile = listOfFiles[i]
                if item.text() == selectedFile:
                    item.setSelected(True)
                    listOfFiles.pop(i)
        pass


    def initUIAction(self):
        self.btnChooseFromPath.clicked.connect(self.choose_src_dir)
        self.btnChooseToPath.clicked.connect(self.choose_dest_dir)
        self.BtnAddFiles.clicked.connect(self.add_files_to_dest)
        self.btnOK.clicked.connect(self.finish_set_task)
        self.btnCancle.clicked.connect(self.cancel_add_task)

        # 设置日期编辑器格式
        self.objDateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.objDateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.objDateTimeEdit.setCalendarPopup(True)  # 设置日历空间允许弹出

        # 设置list的选择模式为多选
        self.listWidgetOfSrc.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        # 设置list的选项动作
        self.listWidgetOfSrc.itemClicked.connect(self.clicked_items_from_src)

    def cancel_add_task(self):
        self.dialog.close()

    def finish_set_task(self):
        """
        if self.destPath == '':
            print(">>:destination path is empty")
            return

        if self.srcPath == '':
            print(">>:source path is empty")
            return
        """

        print("-----task info-----")
        print("task name:" + self.TaskOfName.toPlainText())
        print("src dir:" + self.srcDir)
        print("dest dir:" + self.destDir)
        print("selected items:")
        listOfSelectedItemsName = []
        items = self.listWidgetOfSrc.selectedItems()
        for item in items:
            listOfSelectedItemsName.append(item.text())
            print("item name:" + item.text())

        taskQDateTime = int(self.objDateTimeEdit.dateTime().toTime_t())
        print("-------------------")

        self.__finishToSet = True

        newTask = CpyTask().init_task(
            self.TaskOfName.toPlainText(),
            self.srcPath,
            self.destPath,
            listOfSelectedItemsName,
            taskQDateTime)
        self.taskManager.enqueue(newTask)

        self.after_add_task(newTask)
        self.dialog.close()

    def finish_set(self):
        return self.__finishToSet

    def choose_src_dir(self):
        self.srcDir = QFileDialog.getExistingDirectory(
            self.horizontalLayoutWidget,
            "选取文件夹",
            "./")  # 起始路径
        self.__init_src_dir(self.srcDir)
        """
        self.srcPath = self.srcDir
        self.labSrcPath.setText(self.srcDir)
        self.update_dir_files(self.listWidgetOfSrc, self.srcDir)
        """

    def __init_src_dir(self, path):
        self.srcPath = path
        self.labSrcPath.setText(path)
        self.update_dir_files(self.listWidgetOfSrc, path)

    def choose_dest_dir(self):
        self.destDir = QFileDialog.getExistingDirectory(
            self.horizontalLayoutWidget,
            "选取文件夹",
            "./")  # 起始路径
        self.__init_dest_dir(self.destDir)
        """
        self.destPath = self.destDir
        self.labDestPath.setText(self.destDir)
        self.update_dir_files(self.listWidgetOfDest,
                              self.destDir)
        """

    def __init_dest_dir(self, path):
        self.destPath = path
        self.labDestPath.setText(path)
        self.update_dir_files(self.listWidgetOfDest, path)

    def clicked_items_from_src(self):
        print(self.listWidgetOfSrc.currentItem())
        indexs = self.listWidgetOfSrc.selectedIndexes()
        items = self.listWidgetOfSrc.selectedItems()
        print(indexs)

        self.selectedItems.clear()
        for item in items:
            print(item.text())
            self.selectedItems.append(item.text())

    def add_files_to_dest(self):
        print("source path:" + self.srcPath)
        print("dest path:" + self.destPath)

        if self.destPath == '':
            print(">>:destination path is empty")
            return

        if self.srcPath == '':
            print(">>:source path is empty")
            return

        items = self.listWidgetOfSrc.selectedItems()
        for item in items:
            utils.cpy_file(self.srcPath, self.destPath, item.text())

        self.update_dir_files(self.listWidgetOfDest, self.destPath)

    def update_dir_files(self, vlistOfFiles, directory):
        vlistOfFiles.clear()  # 清空list视窗的内容
        list = os.listdir(directory)  # 列出文件夹下所有的目录与文件
        vlistOfFiles.addItems(list)

    # 删除指定文件
    def do_del_file(self, idx):
        if len(self.listOfSourceFiles) > 0 and idx >= 0:
            delFileName = self.listOfSourceFiles.pop(idx)
            print('>>:del file name:' + delFileName)

            # 如果任务已经开始就需要计时刷新

    def update_task_info(self):
        pass

