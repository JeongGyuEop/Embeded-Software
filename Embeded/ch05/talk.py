# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'talk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TalkWindow(object):
    def setupUi(self, TalkWindow):
        if not TalkWindow.objectName():
            TalkWindow.setObjectName(u"TalkWindow")
        TalkWindow.resize(400, 300)
        self.centralwidget = QWidget(TalkWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setGeometry(QRect(20, 30, 351, 31))
        self.talkMain = QTextEdit(self.centralwidget)
        self.talkMain.setObjectName(u"talkMain")
        self.talkMain.setGeometry(QRect(20, 70, 351, 151))
        self.messageEdit = QLineEdit(self.centralwidget)
        self.messageEdit.setObjectName(u"messageEdit")
        self.messageEdit.setGeometry(QRect(20, 230, 241, 31))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(270, 230, 101, 31))
        TalkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TalkWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        TalkWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TalkWindow)
        self.statusbar.setObjectName(u"statusbar")
        TalkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TalkWindow)

        QMetaObject.connectSlotsByName(TalkWindow)
    # setupUi

    def retranslateUi(self, TalkWindow):
        TalkWindow.setWindowTitle(QCoreApplication.translate("TalkWindow", u"MainWindow", None))
        self.connectButton.setText(QCoreApplication.translate("TalkWindow", u"Connect", None))
        self.sendButton.setText(QCoreApplication.translate("TalkWindow", u"Send", None))
    # retranslateUi

