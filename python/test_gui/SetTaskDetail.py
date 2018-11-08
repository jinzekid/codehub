# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetTaskDetail.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication



class Ui_QDSetTaskDetail(object):
    def setupUi(self, QDSetTaskDetail):
        QDSetTaskDetail.setObjectName("QDSetTaskDetail")
        QDSetTaskDetail.resize(400, 300)
        self.btnOK = QtWidgets.QPushButton(QDSetTaskDetail)
        self.btnOK.setGeometry(QtCore.QRect(280, 10, 113, 32))
        self.btnOK.setObjectName("btnOK")
        self.btnCancle = QtWidgets.QPushButton(QDSetTaskDetail)
        self.btnCancle.setGeometry(QtCore.QRect(280, 40, 113, 32))
        self.btnCancle.setObjectName("btnCancle")

        self.retranslateUi(QDSetTaskDetail)
        QtCore.QMetaObject.connectSlotsByName(QDSetTaskDetail)

    def retranslateUi(self, QDSetTaskDetail):
        _translate = QtCore.QCoreApplication.translate
        QDSetTaskDetail.setWindowTitle(_translate("QDSetTaskDetail", "Dialog"))
        self.btnOK.setText(_translate("QDSetTaskDetail", "确定"))
        self.btnCancle.setText(_translate("QDSetTaskDetail", "取消"))

    def initUIAction(self):
        pass


