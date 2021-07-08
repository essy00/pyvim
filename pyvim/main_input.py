from . import utils

from PyQt5 import QtWidgets
from PyQt5 import QtGui


class MainInput(QtWidgets.QTextEdit):
    def __init__(self, main_window: QtWidgets.QWidget) -> None:
        """
        The normal mode.

        Args:
            main_window (QtWidgets.QWidget): The main window.
        """
        super(MainInput, self).__init__(main_window)

        self.mode = ""
        self.pressed_keys = []
        self.main_window = main_window

        self.setGeometry(
            -5,
            -5,
            self.main_window.width,
            self.main_window.height
        )
        self.setStyleSheet("color: white;")

    def keyPressEvent(self, k: QtGui.QKeyEvent) -> None:
        """
        Triggered when it's typed with an option enabled.

        Args:
            k (QtGui.QKeyEvent): Pressed key.
        """
        key_hex = utils.key_to_hex(k)

        # Checks if the normal mode is enabled.
        if self.mode == "" and not self.isReadOnly():
            if not self.normal_mode_execute(key_hex, self.textCursor()):
                self.pressed_keys.append(key_hex)
        else:
            # Calls super if cannot do an operation
            if not self.insert_mode_execute(key_hex):
                super().keyPressEvent(k)

        # Writes the data.
        try:
            self.print_data(self.textCursor())

        except Exception:
            pass

    def insert_mode_execute(self, key: str) -> bool:
        """
        The operation that is executed when insert mode is enabled.

        Args:
            key (str): Pressed key's hexadecimal value.

        Returns:
            bool: Returns if the key could be executed.
        """
        if key == "0x1000000":  # escape key
            self.setOverwriteMode(True)
            self.mode = ""
        elif key == "0x1000006":  # insert key
            self.setOverwriteMode(not self.overwriteMode())
            self.mode = (
                "-- REPLACE --" if self.overwriteMode() else "-- INSERT --")
        else:
            return False
        return True

    def normal_mode_execute(
        self,
        key: str,
        cursor: QtGui.QTextCursor
    ) -> bool:
        """
        The operation that is executed when normal mode is enabled.

        Args:
            key (int): Pressed key's hexadecimal value.
            cursor (QtGui.QTextCursor): Current cursor.

        Returns:
            bool: Returns if the key could be executed.
        """
        # Moves the cursor
        if key == "0x6c" or key == "0x1000014":  # l or right key
            cursor.movePosition(QtGui.QTextCursor.NextCharacter)

        elif key == "0x4c":  # L
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.movePosition(QtGui.QTextCursor.StartOfLine)

        elif key == "0x68" or key == "0x1000012":  # h or left key
            cursor.movePosition(QtGui.QTextCursor.PreviousCharacter)

        elif key == "0x48":  # H
            cursor.movePosition(QtGui.QTextCursor.Start)

        elif key == "0x6b" or key == "0x1000013":  # k or up key
            cursor.movePosition(QtGui.QTextCursor.Up)

        elif key == "0x4b":  # K
            pass

        elif key == "0x6a" or key == "0x1000015":  # j or down key
            cursor.movePosition(QtGui.QTextCursor.Down)

        elif key == "0x4a":  # J
            pass

        elif key == "0x77":  # w
            cursor.movePosition(QtGui.QTextCursor.NextWord)

        elif key == "0x62":  # b
            cursor.movePosition(QtGui.QTextCursor.PreviousWord)

        elif key == "0x65":  # e
            cursor.movePosition(QtGui.QTextCursor.EndOfWord)

        elif key == "0x30":  # 0
            cursor.movePosition(QtGui.QTextCursor.StartOfLine)

        elif key == "0x24":  # $
            cursor.movePosition(QtGui.QTextCursor.EndOfLine)

        # Opens insert mode
        elif key in utils.INSERT_MODE_KEYS:
            if key == "0x61" or key == "0x1000006":  # a or insert key
                pass

            elif key == "0x41":  # A
                cursor.movePosition(QtGui.QTextCursor.EndOfLine)

            elif key == "0x69":  # i
                cursor.movePosition(QtGui.QTextCursor.PreviousCharacter)

            elif key == "0x49":  # I
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

            self.setOverwriteMode(False)
            self.mode = "-- INSERT --"

        # TODO add o and O
        # TODO add u and Ctrl+r

        # Opens command mode
        elif key == "0x3a":
            self.mode = ""
            self.setReadOnly(True)
            self.main_window.command_text.setReadOnly(False)
            self.main_window.command_text.setFocus(True)
            self.main_window.command_text.setText(":")

        else:
            return False

        self.setTextCursor(cursor)

        return True

    def print_data(self, cursor: QtGui.QTextCursor) -> None:
        """
        Prints the data which is showed on the screen.

        Args:
            cursor (QtGui.QTextCursor): The keyboard cursor.
        """
        self.main_window.position_text.setText(
            f"{cursor.blockNumber()}, {cursor.columnNumber()}"
        )

        # Mode data
        if self.mode == "":
            self.main_window.mode_text.setVisible(False)
        else:
            self.main_window.mode_text.setVisible(True)

        self.main_window.mode_text.setText(
            self.mode
        )
