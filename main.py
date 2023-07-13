# # -*- coding: utf-8 -*-
# # @Author  : LG
# # import os

# from PyQt5 import QtWidgets
# from widgets.mainwindow import MainWindow
# import sys


# if __name__ == '__main__':

#     app = QtWidgets.QApplication([''])
#     mainwindow = MainWindow()
#     mainwindow.show()
#     sys.exit(app.exec_())

from PyQt5 import QtWidgets
from widgets.mainwindow import MainWindow
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='My PyQt5 Application')
    parser.add_argument('--input', help='Input argument')
    default_folder = parser.parse_args()
    app = QtWidgets.QApplication([''])
    # mainwindow = MainWindow()
    mainwindow = MainWindow(default_folder=default_folder)
    mainwindow.show()
    sys.exit(app.exec_())
