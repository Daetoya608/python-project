import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mainwindow

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome_window import Ui_WelcomeWindow

import sys
app = QtWidgets.QApplication(sys.argv)
mainwindow.MainWindow = QtWidgets.QMainWindow()
mainwindow.ui = Ui_WelcomeWindow()
mainwindow.ui.setupUi(mainwindow.MainWindow)
mainwindow.MainWindow.show()
sys.exit(app.exec_())
