import sys
from PySide6.QtWidgets import QApplication
from .position_motor import PositionMotorWindow


def draw_all():
    app = QApplication(sys.argv)
    main_window = PositionMotorWindow()
    main_window.show()
    sys.exit(app.exec())
