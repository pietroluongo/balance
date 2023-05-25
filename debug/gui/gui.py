import sys
from PySide6.QtWidgets import QApplication
from .position_motor import PositionMotorWindow
from .pid_control_window import PIDAdjustmentWindow

def draw_all():
    app = QApplication(sys.argv)
    main_window = PositionMotorWindow()
    pid_window = PIDAdjustmentWindow()
    main_window.show()
    pid_window.show()
    sys.exit(app.exec())
