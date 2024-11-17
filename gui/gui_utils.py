
import mainwindow

def change_window(window_object, *args):
    mainwindow.ui = window_object
    mainwindow.ui.setupUi(mainwindow.MainWindow, *args)
    mainwindow.MainWindow.show()


def set_seller_account(account_ind: int):
    mainwindow.current_seller_account_ind = account_ind