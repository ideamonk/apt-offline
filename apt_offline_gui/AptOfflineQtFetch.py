# -*- coding: utf-8 -*-
import os, sys
from PyQt4 import QtCore, QtGui

from apt_offline_gui.Ui_AptOfflineQtFetch import Ui_AptOfflineQtFetch
from apt_offline_gui.UiDataStructs import GetterArgs
from apt_offline_gui import AptOfflineQtCommon as guicommon
import apt_offline_core.AptOfflineCoreLib


class Worker(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.parent = parent
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        # setup i/o redirects before call
        sys.stdout = self
        sys.stderr = self
        
        apt_offline_core.AptOfflineCoreLib.fetcher(self.args)

    def setArgs (self,args):
        self.args = args

    def write(self, text):
        # redirects console output to our consoleOutputHolder
        # extract chinese whisper from text
      
        if (" / " in text):
            try:
                progress,total = text.split(" / ",1)
                progress = progress.strip()
                total = total.split(" ",1)[0].strip()
                self.emit (QtCore.SIGNAL('progress(QString,QString)'), progress,total)
            except:
                ''' nothing to do '''
        
        self.emit (QtCore.SIGNAL('output(QString)'), text)

    def flush(self):
        ''' nothing to do :D '''


class AptOfflineQtFetch(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AptOfflineQtFetch()
        self.ui.setupUi(self)
        
        # Connect the clicked signal of the Browse button to it's slot
        QtCore.QObject.connect(self.ui.browseFilePathButton, QtCore.SIGNAL("clicked()"),
                        self.popupDirectoryDialog )
                        
        # Connect the clicked signal of the Save to it's Slot - accept
        QtCore.QObject.connect(self.ui.startDownloadButton, QtCore.SIGNAL("clicked()"),
                        self.StartDownload )
                        
        # Connect the clicked signal of the Cancel to it's Slot - reject
        QtCore.QObject.connect(self.ui.cancelButton, QtCore.SIGNAL("clicked()"),
                        self.reject )
                        
        QtCore.QObject.connect(self.ui.profileFilePath, QtCore.SIGNAL("editingFinished()"),
                        self.ControlStartDownloadBox )

        QtCore.QObject.connect(self.ui.profileFilePath, QtCore.SIGNAL("textChanged(QString)"),
                        self.ControlStartDownloadBox )

        self.worker = Worker(parent=self)
        QtCore.QObject.connect(self.worker, QtCore.SIGNAL("output(QString)"),
                        self.updateLog )
        QtCore.QObject.connect(self.worker, QtCore.SIGNAL("progress(QString,QString)"),
                        self.updateProgress )
        
    def popupDirectoryDialog(self):
        # Popup a Directory selection box
        directory = QtGui.QFileDialog.getOpenFileName(self, u'Select the file')
        # Show the selected file path in the field marked for showing directory path
        self.ui.profileFilePath.setText(directory)
        
        self.ControlStartDownloadBox()
        
    def StartDownload(self):
        # Do all the download related work here and then close

        # Clear the consoleOutputHolder
        self.ui.rawLogHolder.setText("")
        
        self.filepath = str(self.ui.profileFilePath.text())

        if os.path.isfile(self.filepath) == False:
            if (len(self.filepath) == 0):
                self.ui.rawLogHolder.setText ( \
                    guicommon.style("Please select a signature file!",'red'))
            else:
                self.ui.rawLogHolder.setText ( \
                    guicommon.style("%s does not exist." % self.filepath,'red'))
            return
        
        # TODO: generate a unique zipfile name
        self.zipfilepath = '/tmp/foozz.zip'
        args = GetterArgs(filename=self.filepath, bundle_file= self.zipfilepath, progress_bar=self.ui.statusProgressBar, progress_label=self.ui.progressStatusDescription)
        
        #returnStatus = apt_offline_core.AptOfflineCoreLib.fetcher(args)
        # TODO: deal with return status laters
        self.worker.setArgs (args)
        self.worker.start()
        #if (returnStatus):
        ''' TODO: do something with self.zipfilepath '''
            
        # TODO to be implemented later
        # self.accept()

    def updateLog(self,text):
        guicommon.updateInto (self.ui.rawLogHolder,text)

    def updateProgress(self,progress,total):
        try:
            # try parsing numbers and updating progressBar
            percent = (float(progress)/float(total))*100
            self.ui.statusProgressBar.setValue (percent)
        except:
            ''' nothing to do '''

    def ControlStartDownloadBox(self):
        if self.ui.profileFilePath.text().isEmpty():
            self.ui.startDownloadButton.setEnabled(False)
        else:
            self.ui.startDownloadButton.setEnabled(True)
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AptOfflineQtFetch()
    myapp.show()
    sys.exit(app.exec_())


