#!/usr/bin/env python3

from .main_input import MainInput
from .command_input import CommandInput
from .text import ModeText, PositionText

from PyQt5 import QtWidgets
import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        """
        Generates the main window.
        """
        super(MainWindow, self).__init__()

        self.width = 600
        self.height = 400

        self.setWindowTitle("Terminal")
        self.resize(self.width, self.height)
        self.setStyleSheet("background-color: black;")

        self.main_text = MainInput(self)
        self.command_text = CommandInput(self)
        self.position_text = PositionText(self)
        self.mode_text = ModeText(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
