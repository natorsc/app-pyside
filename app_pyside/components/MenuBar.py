# -*- coding: utf-8 -*-
"""."""

from PySide6 import QtGui, QtWidgets


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.application = kwargs.get('application')

        self.setObjectName('menu_bar')

        action_exit = QtGui.QAction(
            QtGui.QIcon.fromTheme(
                'application-exit',
                QtGui.QIcon(':/icons/application-exit'),
            ),
            self.tr('Sair'),
            self,
        )
        action_exit.setObjectName('action_exit')
        action_exit.setToolTip(self.tr('Sair do aplicativo.'))
        action_exit.setShortcut(QtGui.QKeySequence('Ctrl+q'))
        action_exit.triggered.connect(self.on_action_exit_triggered)
        action_exit.setCheckable(True)

        menu_file = self.addMenu(self.tr('Arquivo'))
        menu_file.setParent(self)
        menu_file.setObjectName('menu_file')
        menu_file.addAction(action_exit)

    def on_action_exit_triggered(self):
        self.application.exit()
