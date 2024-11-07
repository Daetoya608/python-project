from PyQt5 import QtCore, QtGui, QtWidgets
from app.models.base_account import BaseAccount

ui: object
MainWindow: QtWidgets.QMainWindow

current_account_ind: int = 0
