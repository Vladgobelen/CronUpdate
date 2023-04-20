import sys
import os
from PyQt5 import QtWidgets
import design

cronText = open('/var/spool/cron/crontabs/diver', 'r')


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.textEdit.append (cronText.read())
        cronText.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
     main()
