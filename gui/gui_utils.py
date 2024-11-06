
import mainwindow

def change_window(window_object, *args):
    mainwindow.ui = window_object
    mainwindow.ui.setupUi(mainwindow.MainWindow, *args)
    mainwindow.MainWindow.show()


