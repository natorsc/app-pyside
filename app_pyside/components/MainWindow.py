# -*- coding: utf-8 -*-
"""."""

from PySide6 import QtCore, QtWidgets

try:
    from components.MenuBar import MenuBar
except ModuleNotFoundError:
    from app_pyside.components.MenuBar import MenuBar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.application = kwargs.get('application')

        window_size = QtCore.QSize(683, 384)
        self.resize(window_size)
        self.setMinimumSize(window_size)
        self.setObjectName('main_window')
        self.setWindowTitle(self.tr('Python - PySide6 - Qt'))

        self.setMenuBar(
            MenuBar(
                application=self.application,
            ),
        )

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName('central_widget')
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.label = QtWidgets.QLabel()
        self.label.setObjectName('label')
        self.label.setText(self.tr('Este texto será alterado.'))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setObjectName('line_edit')
        self.line_edit.setPlaceholderText(self.tr('Digite algo.'))
        vbox.addWidget(self.line_edit)

        push_button = QtWidgets.QPushButton()
        push_button.setObjectName('push_button')
        push_button.setText(self.tr('Clique aqui'))
        push_button.clicked.connect(self.on_push_button_clicked)
        vbox.addWidget(push_button)

    def on_push_button_clicked(self, widget):
        text = self.line_edit.text()
        if text.split():
            self.label.setText(text)
        else:
            self.label.setText(self.tr('Digite algo no campo de texto ;).'))


if __name__ == '__main__':
    pass
