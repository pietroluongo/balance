import json

from PySide6.QtWidgets import QMainWindow

from comms import mqtt_sender

from .ui.pid_adjustment import Ui_MainWindow


class PIDAdjustmentWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.p_dial.valueChanged.connect(self._handle_p_dial_change)
        self._ui.i_dial.valueChanged.connect(self._handle_i_dial_change)
        self._ui.d_dial.valueChanged.connect(self._handle_d_dial_change)

        # self._ui.p_dial.setSingleStep(10)
        # self._ui.p_dial.setNotchesVisible(True)
        self._ui.send_m0_btn.clicked.connect(self._handle_send_m0_button)
        self._ui.send_m1_btn.clicked.connect(self._handle_send_m1_button)

    def _handle_p_dial_change(self, val):
        self._ui.p_value.display(f'{val/100:04.2f}')

    def _handle_i_dial_change(self, val):
        self._ui.i_value.display(f'{val/100:04.2f}')

    def _handle_d_dial_change(self, val):
        self._ui.d_value.display(f'{val/100:04.2f}')

    def _handle_send_m0_button(self):
        output = {
            'p': self._ui.p_dial.value()/100,
            'i': self._ui.i_dial.value()/100,
            'd': self._ui.d_dial.value()/100
        }
        mqtt_sender.Sender().publish(json.dumps(output), "/balance/m0/pid")

    def _handle_send_m1_button(self):
        output = {
            'p': self._ui.p_dial.value()/100,
            'i': self._ui.i_dial.value()/100,
            'd': self._ui.d_dial.value()/100
        }
        mqtt_sender.Sender().publish(json.dumps(output), "/balance/m1/pid")
