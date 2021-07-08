from PyQt5 import QtWidgets


class PositionText(QtWidgets.QLabel):
    def __init__(self, main_window: QtWidgets.QWidget) -> None:
        """
        The position text.

        Args:
            main_window (QtWidgets.QWidget): The main window.
        """
        super(PositionText, self).__init__(main_window)

        self.width = 40
        self.height = 15

        self.setGeometry(
            main_window.width - self.width,
            main_window.height - self.height,
            self.width,
            self.height
        )
        self.setStyleSheet("color: white;")

        self.setText("0, 0")


class ModeText(QtWidgets.QLabel):
    def __init__(self, main_window: QtWidgets.QWidget) -> None:
        """
        The mode text.

        Args:
            main_window (QtWidgets.QWidget): The main window.
        """
        super(ModeText, self).__init__(main_window)

        self.width = 100
        self.height = 15

        self.size = 16

        self.setGeometry(
            10,
            main_window.height - self.height,
            self.width,
            self.height
        )
        self.setStyleSheet("color: white;")

        self.setVisible(False)
