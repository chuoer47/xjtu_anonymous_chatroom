# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SafeChatroom(object):
    def setupUi(self, SafeChatroom):
        SafeChatroom.setObjectName("SafeChatroom")
        SafeChatroom.resize(859, 655)
        self.send_window = QtWidgets.QTextEdit(SafeChatroom)
        self.send_window.setGeometry(QtCore.QRect(10, 350, 731, 291))
        self.send_window.setObjectName("send_window")
        self.verticalLayoutWidget = QtWidgets.QWidget(SafeChatroom)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 480, 95, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.send = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.send.setObjectName("send")
        self.verticalLayout.addWidget(self.send)
        self.historySaver = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.historySaver.setObjectName("historySaver")
        self.verticalLayout.addWidget(self.historySaver)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SafeChatroom)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 350, 95, 124))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nickname = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.nickname.setObjectName("nickname")
        self.verticalLayout_2.addWidget(self.nickname)
        self.nickname_changer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.nickname_changer.setObjectName("nickname_changer")
        self.verticalLayout_2.addWidget(self.nickname_changer)
        self.recv_window = QtWidgets.QTextBrowser(SafeChatroom)
        self.recv_window.setGeometry(QtCore.QRect(10, 10, 831, 331))
        self.recv_window.setObjectName("recv_window")
        self.label = QtWidgets.QLabel(SafeChatroom)
        self.label.setGeometry(QtCore.QRect(760, 600, 91, 41))
        self.label.setObjectName("label")

        self.retranslateUi(SafeChatroom)
        QtCore.QMetaObject.connectSlotsByName(SafeChatroom)

    def retranslateUi(self, SafeChatroom):
        _translate = QtCore.QCoreApplication.translate
        SafeChatroom.setWindowTitle(_translate("SafeChatroom", "XJTU 聊天室"))
        self.send.setText(_translate("SafeChatroom", "发送消息"))
        self.historySaver.setText(_translate("SafeChatroom", "保存历史"))
        self.nickname_changer.setText(_translate("SafeChatroom", "修改昵称"))
        self.label.setText(_translate("SafeChatroom", "make by \n"
                                                      " lc lfy"))
