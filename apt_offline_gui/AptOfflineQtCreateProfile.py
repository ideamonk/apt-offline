import sys,os
from PyQt4 import QtCore, QtGui

from apt_offline_gui.Ui_AptOfflineQtCreateProfile import Ui_CreateProfile
from apt_offline_gui.UiDataStructs import SetterArgs
import apt_offline_core.AptOfflineCoreLib


class AptOfflineQtCreateProfile(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CreateProfile()
        self.ui.setupUi(self)
        
        # Connect the clicked signal of the Browse button to it's slot
        QtCore.QObject.connect(self.ui.browseFilePathButton, QtCore.SIGNAL("clicked()"),
                        self.popupDirectoryDialog )
                        
        # Connect the clicked signal of the Save to it's Slot - accept
        QtCore.QObject.connect(self.ui.createProfileButton, QtCore.SIGNAL("clicked()"),
                        self.CreateProfile )
                        
        # Connect the clicked signal of the Cancel to it's Slot - reject
        QtCore.QObject.connect(self.ui.cancelButton, QtCore.SIGNAL("clicked()"),
                        self.reject )
        
        # Disable or Enable the Package List field
        QtCore.QObject.connect(self.ui.installPackagesRadioBox, QtCore.SIGNAL("toggled(bool)"),
                        self.PackageListFieldStatus )
        
    def PackageListFieldStatus(self):
        # If Install Packages Box is selected
        self.isFieldChecked = self.ui.installPackagesRadioBox.isChecked()
        self.ui.packageList.setEnabled(self.isFieldChecked)
    
    def CreateProfile(self):
        # Is the Update requested
        self.updateChecked = self.ui.updateCheckBox.isChecked()
        # Is Upgrade requested
        self.upgradeChecked = self.ui.upgradePackagesRadioBox.isChecked()
        # Is Install Requested
        self.installChecked = self.ui.installPackagesRadioBox.isChecked()
        
        # If atleast one is requested
        if self.updateChecked or self.upgradeChecked or self.installChecked:
            self.filepath=self.ui.profileFilePath.text()
            if self.installChecked:
                self.packageList = self.ui.packageList.split(",")
            else:
                self.packageList = None
            args = SetterArgs(filename=self.filepath, update=self.updateChecked, upgrade=self.upgradeChecked, install_packages=self.packageList)
            apt_offline_core.AptOfflineCoreLib.setter(args)
        else:
            pass
        
    
    def popupDirectoryDialog(self):
        # Popup a Directory selection box
        signatureFilePath = os.path.expanduser("~")+"/Desktop/"+"apt-offline.sig"
        directory = QtGui.QFileDialog.getSaveFileName(self, u'Select a filename to save the signature', signatureFilePath, "apt-offline Signatures (*.sig)")
        # Show the selected file path in the field marked for showing directory path
        self.ui.profileFilePath.setText(directory)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AptOfflineQtCreateProfile()
    myapp.show()
    sys.exit(app.exec_())
