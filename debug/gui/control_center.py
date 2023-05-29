from PySide6.QtWidgets import QMainWindow

from .ui.command_center import Ui_MainWindow
from .position_motor import PositionMotorWindow
from .pid_control_window import PIDAdjustmentWindow
from .console import Console

class ControlCenter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._position_motor_window = PositionMotorWindow()
        self._pid_window = PIDAdjustmentWindow()
        self._console_window = Console()

        self._ui.motor_control.clicked.connect(self._handle_motor_control)
        self._ui.pid_adjust.clicked.connect(self._handle_pid_adjust)
        self._ui.console.clicked.connect(self._handle_console)


    def _handle_motor_control(self):
        self._position_motor_window.show()

    def _handle_pid_adjust(self):
        self._pid_window.show()

    def _handle_console(self):
        self._console_window.show()