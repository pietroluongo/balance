from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from .ui.ui_motor_positioning import Ui_MainWindow


class PositionMotorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._link_slider_update_functions()
        self._set_initial_state()
        self._ui.checkBox.stateChanged.connect(self._handle_auto_mode_toggle)
        self._ui.radioButton.toggled.connect(self._handle_auto_mode_toggle)

    def _set_initial_state(self):
        self._ui.radioButton_2.setChecked(True)
        self._ui.verticalSlider.setEnabled(False)
        self._ui.horizontalSlider.setEnabled(False)

    def _link_slider_update_functions(self):
        self._ui.verticalSlider.valueChanged.connect(self._set_vertical_slider_val)
        self._ui.horizontalSlider.valueChanged.connect(self._set_horizontal_slider_val)
        self._ui.verticalSlider.setEnabled(True)
        self._ui.horizontalSlider.setEnabled(True)

    def _unlink_slider_update_functions(self):
        self._ui.verticalSlider.valueChanged.disconnect()
        self._ui.horizontalSlider.valueChanged.disconnect()
        self._ui.verticalSlider.setEnabled(False)
        self._ui.horizontalSlider.setEnabled(False)

    def _handle_auto_mode_toggle(self):
        if self._ui.radioButton.isChecked():
            self._link_slider_update_functions()
        else:
            self._unlink_slider_update_functions()

    def _set_vertical_slider_val(self, val):
        self._ui.label_4.setText("{0:+04.2f}".format((val - 50) * 180 / 100))

    def _set_horizontal_slider_val(self, val):
        self._ui.label_3.setText("{0:+04.2f}".format((val - 50) * 180 / 100))

    def enable_active_mode(self):
        self._link_slider_update_functions()

    def disable_active_mode(self):
        self._unlink_slider_update_functions()
        self._ui.verticalSlider.setEnabled(False)
        self._ui.horizontalSlider.setEnabled(False)
