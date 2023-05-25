from PySide6.QtWidgets import QMainWindow
from .ui.pid_adjustment import Ui_MainWindow

class PIDAdjustmentWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.p_dial.valueChanged.connect(self._handle_p_dial_change)
        self._ui.p_dial.setSingleStep(10)
        self._ui.p_dial.setNotchesVisible(True)

    def _handle_p_dial_change(self, val):
        self._ui.p_value.display(f'{val/100:04.2f}')