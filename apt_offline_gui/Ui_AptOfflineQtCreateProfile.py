# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtCreateProfile.ui'
#
# Created: Thu Feb  4 01:28:54 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CreateProfile(object):
    def setupUi(self, CreateProfile):
        CreateProfile.setObjectName("CreateProfile")
        CreateProfile.resize(420, 368)
        self.verticalLayoutWidget = QtGui.QWidget(CreateProfile)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 309))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblInstallType = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblInstallType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblInstallType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblInstallType.setObjectName("lblInstallType")
        self.verticalLayout_3.addWidget(self.lblInstallType)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.updateCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.updateCheckBox.setObjectName("updateCheckBox")
        self.verticalLayout_4.addWidget(self.updateCheckBox)
        self.upgradePackagesRadioBox = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.upgradePackagesRadioBox.setObjectName("upgradePackagesRadioBox")
        self.verticalLayout_4.addWidget(self.upgradePackagesRadioBox)
        self.installPackagesRadioBox = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.installPackagesRadioBox.setObjectName("installPackagesRadioBox")
        self.verticalLayout_4.addWidget(self.installPackagesRadioBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblPackageList = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPackageList.setObjectName("lblPackageList")
        self.horizontalLayout_6.addWidget(self.lblPackageList)
        self.packageList = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.packageList.setEnabled(False)
        self.packageList.setMinimumSize(QtCore.QSize(0, 30))
        self.packageList.setReadOnly(False)
        self.packageList.setObjectName("packageList")
        self.horizontalLayout_6.addWidget(self.packageList)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblSaveProfile = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblSaveProfile.setObjectName("lblSaveProfile")
        self.horizontalLayout_3.addWidget(self.lblSaveProfile)
        self.profileFilePath = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.profileFilePath.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileFilePath.sizePolicy().hasHeightForWidth())
        self.profileFilePath.setSizePolicy(sizePolicy)
        self.profileFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.profileFilePath.setObjectName("profileFilePath")
        self.horizontalLayout_3.addWidget(self.profileFilePath)
        self.browseFilePathButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.browseFilePathButton.setMinimumSize(QtCore.QSize(0, 30))
        self.browseFilePathButton.setObjectName("browseFilePathButton")
        self.horizontalLayout_3.addWidget(self.browseFilePathButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblConsoleOutput = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblConsoleOutput.setObjectName("lblConsoleOutput")
        self.verticalLayout_8.addWidget(self.lblConsoleOutput)
        self.consoleOutputHolder = QtGui.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleOutputHolder.sizePolicy().hasHeightForWidth())
        self.consoleOutputHolder.setSizePolicy(sizePolicy)
        self.consoleOutputHolder.setMinimumSize(QtCore.QSize(0, 100))
        self.consoleOutputHolder.setMaximumSize(QtCore.QSize(16777215, 100))
        self.consoleOutputHolder.setObjectName("consoleOutputHolder")
        self.verticalLayout_8.addWidget(self.consoleOutputHolder)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayoutWidget = QtGui.QWidget(CreateProfile)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(11, 320, 401, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.createProfileButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.createProfileButton.setEnabled(True)
        self.createProfileButton.setMinimumSize(QtCore.QSize(100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createProfileButton.setIcon(icon)
        self.createProfileButton.setObjectName("createProfileButton")
        self.horizontalLayout_4.addWidget(self.createProfileButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)

        self.retranslateUi(CreateProfile)
        QtCore.QMetaObject.connectSlotsByName(CreateProfile)

    def retranslateUi(self, CreateProfile):
        CreateProfile.setWindowTitle(QtGui.QApplication.translate("CreateProfile", "Create Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInstallType.setText(QtGui.QApplication.translate("CreateProfile", "Installation Type", None, QtGui.QApplication.UnicodeUTF8))
        self.updateCheckBox.setText(QtGui.QApplication.translate("CreateProfile", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.upgradePackagesRadioBox.setText(QtGui.QApplication.translate("CreateProfile", "Upgrade Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.installPackagesRadioBox.setText(QtGui.QApplication.translate("CreateProfile", "Install Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPackageList.setText(QtGui.QApplication.translate("CreateProfile", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install these packages</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">separate by comma</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSaveProfile.setText(QtGui.QApplication.translate("CreateProfile", "Save Profile As ", None, QtGui.QApplication.UnicodeUTF8))
        self.browseFilePathButton.setText(QtGui.QApplication.translate("CreateProfile", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.lblConsoleOutput.setText(QtGui.QApplication.translate("CreateProfile", "Console Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.createProfileButton.setText(QtGui.QApplication.translate("CreateProfile", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("CreateProfile", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc