from PySide6.QtWidgets import QMainWindow

from .ui.console import Ui_MainWindow

class Console(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)