# -*- coding: utf-8 -*-
"""."""

import sys
import unittest

from PySide6 import QtWidgets

from app_pyside.components.MainWindow import MainWindow


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        if not QtWidgets.QApplication.instance():
            application = QtWidgets.QApplication(sys.argv)
        else:
            application = QtWidgets.QApplication.instance()
        self.mainwindow = MainWindow()

    def test_label_object_name(self):
        assert self.mainwindow.label.objectName() == 'label'

    def test_line_edit_object_name(self):
        assert self.mainwindow.line_edit.objectName() == 'line_edit'


if __name__ == '__main__':
    unittest.main()
