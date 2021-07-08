from . import utils

from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys


class CommandInput(QtWidgets.QLineEdit):
    def __init__(self, main_window: QtWidgets.QWidget) -> None:
        """
        The command mode.

        Args:
            main_window (QtWidgets.QWidget): The main window.
        """
        super(CommandInput, self).__init__(main_window)

        self.main_window = main_window

        self.width = 200
        self.height = 20

        self.setGeometry(
            0,
            self.main_window.height - self.height,
            self.width,
            self.height
        )

        self.setStyleSheet("color: white; border: none")

        self.setReadOnly(True)
        self.setText("")

    def keyPressEvent(self, k: QtGui.QKeyEvent) -> None:
        """
        Triggered when it's typed without any option enabled.

        Args:
            k (QtGui.QKeyEvent): Pressed key.
        """
        key_hex = utils.key_to_hex(k)

        if not self.isReadOnly():
            if key_hex == "0x1000000":
                pass
            elif key_hex == "0x1000004":
                self.execute_command(self.text())
            super().keyPressEvent(k)

        # Opens normal mode
        if key_hex == "0x1000000" or self.text() == "":
            self.setReadOnly(True)
            self.setText("")
            self.main_window.main_text.setFocus(True)
            self.main_window.main_text.setReadOnly(False)

    def execute_command(self, text: str) -> None:
        """
        Executes the command.

        Args:
            text (str): The complete command.
        """
        user_input = text.replace(":", "").split(" ")

        command = list(user_input[0])

        if "w" in command:
            try:
                self.save(
                    user_input[1],
                    self.main_window.main_text.toPlainText()
                )
            except Exception:
                pass

        if "q" in command:
            self.exit()

        self.setReadOnly(True)
        self.setText("")
        self.main_window.main_text.setFocus(True)
        self.main_window.main_text.setReadOnly(False)

    def exit(self) -> None:
        """
        Exits the application.
        """
        sys.exit()

    def save(self, filename: str, text: str) -> None:
        """
        Saves the file.

        Args:
            filename (str): The file name
            text (str): The text
        """
        file = open(filename, "w")

        for line in text.split("\n"):
            file.write(f"{line}\n")

        file.close()
