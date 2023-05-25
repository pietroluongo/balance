from PyQt5.QtWidgets import QWidget, QLabel
from .constants import WIDTH, HEIGHT
from comms.mqtt_sender import Sender

class ConnectionStatus:
    def __init__(self, parent: QWidget):
        self._init_static_label(parent)
        self._draw_connection_status(parent)

    def _init_static_label(self, parent: QWidget):
        text_label = QLabel(parent)
        text_label.setText("MQTT Connection Status: ")
        text_label.move(WIDTH - 250, HEIGHT - 20)
        text_label.show()
        self._static_label = text_label

    def _draw_connection_status(self, parent: QWidget):
        status_label = QLabel(parent)
        status_label.setText("Not Connected")
        status_label.setStyleSheet("color: rgb(255, 0, 0);")
        status_label.move(WIDTH - 100, HEIGHT - 20)
        status_label.show()
        self._status_label = status_label
        # sender = Sender
        # sender.register_connect_callback(sender, self.set_is_connected)

    def _set_is_connected_callback(self):
        pass

    def set_is_connected(self, is_connected: bool):
        if is_connected:
            self._status_label.setText("Connected")
            self._status_label.setStyleSheet("color: rgb(0, 150, 0);")
        else:
            self._status_label.setText("Not Connected")
            self._status_label.setStyleSheet("color: rgb(255, 0, 0);")
