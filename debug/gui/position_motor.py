from enum import Enum
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from comms.mqtt_sender import Sender
from .ui.ui_motor_positioning import Ui_MainWindow


class Motor(Enum):
    M0 = 0
    M1 = 1


class PositionMotorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._link_slider_update_functions()
        self._set_initial_state()
        self._ui.radioButton.toggled.connect(self._handle_readonly_mode_toggle)
        self._ui.checkBox.toggled.connect(self._handle_automatic_update_mode_change)
        self._automatic_update = False
        self._sender = Sender()

    def _set_initial_state(self):
        self._ui.radioButton_2.setChecked(True)
        self._ui.verticalSlider.setEnabled(False)
        self._ui.horizontalSlider.setEnabled(False)
        self._ui.checkBox.setChecked(False)
        self._ui.checkBox.setEnabled(False)

    def _link_slider_update_functions(self):
        self._ui.verticalSlider.valueChanged.connect(self._set_vertical_slider_val)
        self._ui.horizontalSlider.valueChanged.connect(self._set_horizontal_slider_val)
        self._ui.horizontalSlider.sliderReleased.connect(self._handle_horizontal_slider_mouseup)
        self._ui.verticalSlider.sliderReleased.connect(self._handle_vertical_slider_mouseup)
        self._ui.verticalSlider.setEnabled(True)
        self._ui.horizontalSlider.setEnabled(True)

    def _lock_sliders(self):
        self._ui.verticalSlider.setEnabled(False)
        self._ui.horizontalSlider.setEnabled(False)

    def _handle_readonly_mode_toggle(self):
        if self._ui.radioButton.isChecked():
            self._link_slider_update_functions()
            self._ui.checkBox.setEnabled(True)
        else:
            self._lock_sliders()
            self._ui.checkBox.setEnabled(False)

    def _handle_automatic_update_mode_change(self, val: Qt.CheckState):
        self._automatic_update = val == bool(Qt.CheckState.Checked)

    @staticmethod
    def _convert_to_deg(val: int) -> float:
        return (val - 50) * 180 / 100

    def _set_vertical_slider_val(self, val):
        tgt_val = PositionMotorWindow._convert_to_deg(val)
        self._ui.label_4.setText(f"{tgt_val:+04.2f}")
        if self._automatic_update:
            self._dispatch_motor_command(tgt_val, Motor.M0)

    def _set_horizontal_slider_val(self, val):
        tgt_val = PositionMotorWindow._convert_to_deg(val)
        self._ui.label_3.setText(f"{tgt_val:+04.2f}")
        if self._automatic_update:
            self._dispatch_motor_command(tgt_val, Motor.M1)

    def _dispatch_motor_command(self, val: float, motor: Motor):
        if motor == Motor.M0:
            self._sender.publish(str(val), "/balance/debug/setM0")
        else:
            self._sender.publish(str(val), "/balance/debug/setM1")

    def _handle_vertical_slider_mouseup(self):
        if not self._automatic_update:
            self._dispatch_motor_command(PositionMotorWindow._convert_to_deg(self._ui.verticalSlider.value()), Motor.M0)

    def _handle_horizontal_slider_mouseup(self):
        print("horizontal slider mouseup")
        if not self._automatic_update:
            self._dispatch_motor_command(PositionMotorWindow._convert_to_deg(self._ui.horizontalSlider.value()), Motor.M1)
